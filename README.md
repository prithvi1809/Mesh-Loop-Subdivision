# Binary Loop Subdivision on Mesh Surfaces

## Overview
This project focuses on implementing binary Loop subdivision surfaces on mesh models using a Python halfedge data structure. The goal is to achieve smooth and refined subdivision surfaces based on the binary Loop subdivision algorithm. Two well-known 3D models, Utah’s teapot and Stanford’s bunny, are used for testing and demonstration.

## Testing Data
1. Utah’s Teapot Model
2. Stanford’s Bunny Model

## Software Library
The implementation utilizes a Python halfedge data structure software library, and the main code is provided in `Test.py`. The supported mesh formats include .m, .obj, and .off. To visualize the results, a free .obj/.off file viewer can be downloaded from [MeshLab](http://meshlab.sourceforge.net/), while .m files can be visualized using G3DOGL.

## Outputs
The project provides the following outputs:
1. **Loop Subdivision Implementation Source Code Package**: The complete source code package for the binary Loop subdivision implementation, ready for compilation.
2. **Subdivision Surface Results (One Iteration)**: Mesh results in .obj format after one iteration of the binary Loop subdivision.
3. **Subdivision Surface Results (Two Iterations)**: Mesh results in .obj format after two iterations of the binary Loop subdivision.

## How to Use
1. Clone the repository.
2. Ensure you have the required Python environment.
3. Run `Test.py` to execute the binary Loop subdivision on the chosen mesh models.
4. Visualize the results using the recommended file viewers.

### Project Structure
- **test/data/**: Includes the Utah teapot and Stanford bunny models in supported formats.
- **output/**: Stores the subdivision surface results after each iteration.
- **images/**: Contains snapshot of the six visualizations.

### Getting Started
1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/prithvi1809/Mesh-Loop-Subdivision.git
2. Run the main code.
    ```bash
    python Test.py
## Visualizations

![Subdivision Bunny]("output\images\snapshot100.png")

**Bunny Model**
<table>
  <tr>
    <td align="center"><img src="output\images\snapshot00.png" alt="Image 2" /><br/>After 1 Iteration</td>
    <td align="center"><img src="output\images\snapshot200.png" alt="Image 3" /><br/>After 2 Iteration</td>
  </tr>
</table>

![Subdivision BunnyCloud](output\images\snapshotB01.png)
**Point Cloud**

![Subdivision Teapot](output\images\snapshot300.png)
**Teapot Model** 
<table>
  <tr>
    <td align="center"><img src="output\images\snapshot400.png" alt="Image 4" />After 1 Iteration</td>
    <td align="center"><img src="output\images\snapshot500.png" alt="Image 5" /><br/>After 2 Iteration</td>
  </tr>
</table>

![Subdivision TeapotCloud](output\images\snapshotT01.png)
**Point Cloud**

## Note
Ensure that the mesh models are appropriately referenced in the code, and adjust the file paths as needed.
Feel free to explore and experiment with different mesh models and parameters to observe the effects of binary Loop subdivision on various 3D geometries.
