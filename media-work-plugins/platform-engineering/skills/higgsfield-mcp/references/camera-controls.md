# Camera Controls

Supported camera movements for post-processing generated video.

## Available Controls

| Control | Description |
|---------|-------------|
| `zoom_in` | Gradual zoom toward subject |
| `zoom_out` | Gradual zoom away from subject |
| `pan_left` | Horizontal pan to the left |
| `pan_right` | Horizontal pan to the right |
| `orbit` | Circular orbit around subject |
| `dolly` | Forward/backward dolly movement |

## Usage

Apply camera controls after initial video generation by calling the post-processing endpoint with the generated video file and desired camera movement parameters.
