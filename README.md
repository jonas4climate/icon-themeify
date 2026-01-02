# Icon Themeify

This tool serves for procedurally generating themed icons from original app icon images. The main use case revolves around generating icons for consistently themed app pages for iOS, iPadOS and macOS devices, for aesthetics purposes. While commonly used icons are available on various platforms, less widely used apps do not have such themed icons available, resulting in the need to create them in an automated manner.

## Showcase using `AllTrails`

<table>
  <tr>
    <td width="20%" valign="top" align="center">
      <p><strong>Original Icon</strong></p>
      <table width="100%">
        <tr>
          <td width="100%" align="center">
            <img src="example/alltrails.webp" alt="Original icon" width="100%" />
          </td>
        </tr>
      </table>
    </td>
    <td width="60%" valign="top">
      <p align="center"><strong>Themed Icons</strong></p>
      <table width="100%">
        <tr>
          <td width="33%" align="center">
            <img src="example/alltrails_light.png" alt="Light-themed icon" width="90%" />
          </td>
          <td width="33%" align="center">
            <img src="example/alltrails_blue.png" alt="Blue-themed icon" width="90%" />
          </td>
          <td width="33%" align="center">
            <img src="example/alltrails_dark.png" alt="Dark-themed icon" width="90%" />
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>

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

