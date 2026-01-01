from PIL import Image
import cv2
import numpy as np
from skimage.morphology import skeletonize, dilation, disk


def simplify_icon(input_path, output_path, base_color, edge_color, line_thickness: int = 1, min_elem_size: int = 100, edge_free_pad: int = 10, show_process: bool = False):
    # Load the image
    img = Image.open(input_path)
    img = img.convert('RGBA')
    img_array = np.array(img)
    if show_process:
        import matplotlib.pyplot as plt
        images, descriptions = [], []
        images.append(img_array.copy())
        descriptions.append("Original")

    # Separate RGB and alpha channels
    rgb = img_array[:, :, :3]
    alpha = img_array[:, :, 3]

    # Convert to grayscale
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    if show_process:
        images.append(np.stack([gray]*3, axis=-1))
        descriptions.append("Grayscale")

    # Apply Canny edge detection
    edges = cv2.Canny(gray, 100, 200)
    if show_process:
        images.append(np.stack([edges]*3, axis=-1))
        descriptions.append("Edge detection")

    # Skeletonize the edges
    skeleton = skeletonize(edges // 255)  # Convert to binary for skeletonize
    skeleton = skeleton.astype(np.uint8) * 255  # Convert back to 0-255 range
    if show_process:
        images.append(np.stack([skeleton]*3, axis=-1))
        descriptions.append("Skeletonization")

    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(skeleton, connectivity=8)
    for i in range(1, num_labels):
        if stats[i, cv2.CC_STAT_AREA] < min_elem_size:
            skeleton[labels == i] = 0
    if show_process:
        images.append(np.stack([skeleton]*3, axis=-1))
        descriptions.append("Size filter")

    skeleton = dilation(skeleton, disk(line_thickness))
    if show_process:
        images.append(np.stack([skeleton]*3, axis=-1))
        descriptions.append("Line dilation")

    # Create an RGBA image with the thickened skeletonized edges
    edges_rgba = np.zeros_like(img_array)
    edges_rgba[:, :, :3] = skeleton[:, :, np.newaxis]  # RGB
    edges_rgba[:, :, 3] = alpha # Alpha
    if show_process:
        images.append(edges_rgba.copy())
        descriptions.append("Shape preservation")

    mask = (edges_rgba[:, :, 0] > 0)
    edges_rgba[mask, :3] = edge_color
    edges_rgba[~mask, :3] = base_color
    if show_process:
        images.append(edges_rgba.copy())
        descriptions.append("Color")

    # Find all pixels whose distance to the transparent area is less than 10 pixels
    transparent_mask = (alpha == 0)
    distance_transform = cv2.distanceTransform((~transparent_mask).astype(np.uint8), cv2.DIST_L2, 5)
    close_to_transparent = (distance_transform < edge_free_pad)
    edges_rgba[close_to_transparent, :3] = base_color
    if show_process:
        images.append(edges_rgba.copy())
        descriptions.append("Edge padding (1)")

    # Find all pixels whose distance to the image edge is less than 10 pixels
    edge_mask = np.zeros_like(alpha, dtype=bool)
    edge_mask[:10, :] = True
    edge_mask[-10:, :] = True
    edge_mask[:, :10] = True
    edge_mask[:, -10:] = True
    distance_to_edge = cv2.distanceTransform((~edge_mask).astype(np.uint8), cv2.DIST_L2, 5)
    close_to_image_edge = (distance_to_edge < edge_free_pad)
    edges_rgba[close_to_image_edge, :3] = base_color
    if show_process:
        images.append(edges_rgba.copy())
        descriptions.append("Edge padding (2)")
        images.append(edges_rgba.copy())
        descriptions.append("Final image")

    if show_process:
        n = len(images)
        cols = 6
        rows = (n + cols - 1) // cols
        plt.figure(figsize=(4 * cols, 4 * rows))
        for i, image in enumerate(images):
            plt.subplot(rows, cols, i + 1)
            plt.title(descriptions[i])
            if image.shape[2] == 4:
                plt.imshow(image)
            else:
                plt.imshow(image, cmap='gray')
            plt.axis('off')
        plt.tight_layout()
        plt.savefig(output_path.parent / f"{output_path.stem}_process.png")
        plt.close()


    result = Image.fromarray(edges_rgba)
    result.save(output_path)
