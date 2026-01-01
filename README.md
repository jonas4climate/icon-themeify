# Icon Themeify

This tool serves for procedurally generating themed icons from original app icon images. The main use case revolves around generating icons for consistently themed app pages for iOS, iPadOS and macOS devices, for aesthetics purposes. While commonly used icons are available on various platforms, less widely used apps do not have such themed icons available, resulting in the need to create them in an automated manner.

## Showcase using `AllTrails`

<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
  <!-- First image with its own title -->
  <div style="text-align: center; width: 24%;">
    <p><strong>Original Icon</strong></p>
    <img src="example/alltrails.webp" alt="Original icon" style="width: 100%;" />
  </div>

  <!-- Shared title for the next three images -->
  <div style="width: 72%;">
    <p style="text-align: center;"><strong>Themed Icons</strong></p>
    <div style="display: flex; justify-content: space-between;">
      <img src="example/alltrails_light.png" alt="Light-themed icon" style="width: 32%;" />
      <img src="example/alltrails_blue.png" alt="Blue-themed icon" style="width: 32%;" />
      <img src="example/alltrails_dark.png" alt="Dark-themed icon" style="width: 32%;" />
    </div>
  </div>
</div>

<br>
<hr>
<br>

### Process

<div align="center">
  <img src="example/alltrails_process.png" alt="Description" width="100%" />
</div>

## Setup

Download the tool as common practice using pip or consider cloning the repository to make use of the base configuration files and examples.

## Usage

1. Download the original source image of the app icon, e.g. here for [AllTrails](https://apps.apple.com/us/app/alltrails-hike-bike-run/id405075943)
2. Run the CLI using `python cli.py -i <input-path> -o <output-path>`

