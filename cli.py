import argparse
from pathlib import Path

from src.themeify.theme import ThemeConfig
from src.themeify.core import simplify_icon

SUPPORTED_MEDIA_FORMATS = ['.png', '.jpg', '.jpeg', '.webp']

def main():
    parser = argparse.ArgumentParser(description="Convert images from app icons into themed icons")
    parser.add_argument("-t", "--themes", dest="themes_config", required=False, help="Path to the themes config")
    parser.add_argument("-f", "--format", dest="image_format", required=False, default="png", help="Output image format (default: png)")
    parser.add_argument("-i", "--input", dest="input_path", required=False, default="input", help="Input directory (default: input)")
    parser.add_argument("-o", "--output", dest="output_path", required=False, default="output", help="Output directory (default: output)")
    args = parser.parse_args()

    # Handle inputs
    input_path = Path(args.input_path)
    if not input_path.exists():
        raise FileNotFoundError(f"Input path {args.input_path} does not exist.")
    input_files = []
    if input_path.is_file():
        input_files.append(input_path)
    elif input_path.is_dir():
        for ext in SUPPORTED_MEDIA_FORMATS:
            input_files.extend(input_path.glob(f'*{ext}'))
        if len(input_files) == 0:
            raise FileNotFoundError(f"No supported image files found in input path {args.input_path}.")
        
    img_format = args.image_format.lower()
    if f".{img_format}" not in SUPPORTED_MEDIA_FORMATS:
        raise ValueError(f"Unsupported image format: {img_format}. Supported formats are: {SUPPORTED_MEDIA_FORMATS}")
        
    output_path = Path(args.output_path)

    if args.themes_config:
        json_text = Path(args.themes_config).read_text()
        themes = ThemeConfig.model_validate_json(json_text).themes
    else: # default
        themes = ThemeConfig().themes
        
    for theme in themes:
        base_path = output_path / theme.name
        base_path.mkdir(parents=True, exist_ok=True)
        for i, input_file in enumerate(input_files):
            output_file = base_path / f"{input_file.stem}.{img_format}"
            simplify_icon(
                input_file, 
                output_file, 
                theme.base_rgb, 
                theme.edge_rgb, 
                line_thickness=theme.line_thickness, 
                min_elem_size=theme.min_elem_size, 
                edge_free_pad=theme.edge_free_pad, 
                show_process=True
            )

    
if __name__ == "__main__":
    main()


# output_format = 'webp'

# for theme in themes:
#     base_path = Path('output') / theme.name
#     base_path.mkdir(parents=True, exist_ok=True)
#     for i, input_file in enumerate(Path('input').glob('*.webp')):
#         output_file = base_path / f"{input_file.stem}.{output_format}"
#         simplify_icon(input_file, output_file, theme.base_rgb, theme.edge_rgb, line_thickness=theme.line_thickness, min_elem_size=theme.min_elem_size, edge_free_pad=theme.edge_free_pad, show_process=True)
