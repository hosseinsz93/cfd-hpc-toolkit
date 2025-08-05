# CFD HPC Toolkit

A collection of Python scripts for monitoring and visualizing Computational Fluid Dynamics (CFD) simulations on high-performance computing (HPC) clusters.

## 🚀 Overview

This toolkit provides real-time plotting and analysis tools for CFD simulations, designed to work across multiple HPC environments including Zagros, and Seawulf @SBU. All scripts feature automatic cluster detection, conda environment support, and robust gnuplot integration.

## 📊 Available Tools

### Plotting Scripts

| Script | Purpose | Key Metrics |
|--------|---------|-------------|
| `plotKE` | Kinetic Energy monitoring | Energy evolution over time steps |
| `plotConverge` | Convergence analysis | Momentum and Poisson residuals |
| `plotTime` | Performance timing | Solver timing breakdown (Momentum, Poisson, Concentration, Total) |
| `plotCourant` | Stability monitoring | Courant numbers for numerical stability |
| `plotConc` | Concentration tracking | Species concentration evolution |
| `plotFlux` | Flow analysis | Mass/momentum flux monitoring |
| `plotTemp` | Temperature analysis | Temperature field evolution |

### Utility Scripts

| Script | Purpose | Description |
|--------|---------|-------------|
| `calcTime` | Time calculation | Calculate simulation timing statistics |
| `lastTimeStep.py` | Status checking | Extract latest time step information |
| `meminfo` | Memory monitoring | System memory usage tracking |
| `submit` | Job submission | HPC job submission wrapper |
| `writeProt` | File protection | Write protection utilities |

### Data Management

| Script | Purpose | Description |
|--------|---------|-------------|
| `copyfromzagros` | Data transfer | Copy data from Zagros cluster |
| `copytozagros` | Data transfer | Copy data to Zagros cluster |
| `rclone` | Cloud sync | Cloud storage synchronization |
| `unison` | File sync | Bidirectional file synchronization |
| `fpzip` | Compression | High-performance data compression |
| `dfg` | Data format | Data format conversion utilities |
| `dug` | Data utilities | Data manipulation tools |

## 🖥️ Supported Clusters

- **Zagros** (`zagros.cewit.stonybrook.edu`)
- **Seawulf** (Stony Brook SeaWulf cluster)
- **Custom Clusters** (IP-based detection)

## 🛠️ Installation

### Prerequisites

- Python 2.7+ or Python 3.x
- Gnuplot for visualization
- Conda (recommended for gnuplot installation)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hosseinsz93/cfd-hpc-toolkit.git
   cd cfd-hpc-toolkit
   ```

2. **Install gnuplot using conda:**
   ```bash
   conda create -n gnuplot-env gnuplot
   conda activate gnuplot-env
   ```

3. **Make scripts executable:**
   ```bash
   chmod +x plot* calc* last* mem* submit write*
   ```

4. **Add to PATH (optional):**
   ```bash
   export PATH=$PATH:/path/to/cfd-hpc-toolkit
   ```

## 📈 Usage

### Real-time Monitoring

All plotting scripts support real-time monitoring with automatic refresh:

```bash
# Monitor kinetic energy (refreshes every 30 seconds)
plotKE 

# Monitor convergence with custom refresh rate
plotConverge 

# Monitor timing performance
plotTime 

# Monitor Courant numbers for stability
plotCourant 
```

### Custom Plotting Options

```bash
# Set plot ranges
./plotKE -y 100                    # Set max Y to 100
./plotTime -x 1000 --miny 10       # Set max X to 1000, min Y to 10
./plotConverge -x 500 -y 1e-6      # Custom X and Y ranges

# Force PNG output (for headless systems)
./plotKE -p                        # Saves plot as PNG file
```

### Data Analysis

```bash
# Calculate timing statistics
calcTime Converge_dU

# Get latest time step info
python lastTimeStep.py

# Check memory usage
meminfo
```

## 🔧 Features

### Automatic Cluster Detection
- Detects cluster environment automatically
- Supports multiple gnuplot installations
- Handles conda environments seamlessly

### Real-time Visualization
- Live updating plots with customizable refresh rates
- Interactive X11 displays when available
- Automatic fallback to PNG output for headless systems

### Robust Error Handling
- Graceful handling of missing files
- Python 2/3 compatibility
- Clear error messages and debugging output

### Performance Monitoring
- Track solver performance over time
- Monitor numerical stability (Courant numbers)
- Analyze convergence behavior

## 📁 File Structure

```
cfd-hpc-toolkit/
├── README.md              # This file
├── plotKE                 # Kinetic energy plotting
├── plotConverge           # Convergence monitoring  
├── plotTime               # Performance timing
├── plotCourant            # Courant number analysis
├── plotConc               # Concentration tracking
├── plotFlux               # Flux monitoring
├── plotTemp               # Temperature analysis
├── calcTime               # Timing calculations
├── lastTimeStep.py        # Latest time step info
├── meminfo                # Memory monitoring
├── submit                 # Job submission
├── writeProt              # File protection
├── copyfromzagros         # Data transfer from Zagros
├── copytozagros           # Data transfer to Zagros
├── rclone                 # Cloud synchronization
├── unison                 # File synchronization
├── fpzip                  # Data compression
├── dfg                    # Data format utilities
└── dug                    # Data manipulation
```

## 🎯 Common Use Cases

### 1. Monitoring Long-Running Simulations
```bash
# Start monitoring in background
nohup plotConverge -r 300 &  # Check every 5 minutes
nohup plotKE -r 300 &
```

### 2. Performance Analysis
```bash
# Analyze solver timing
plotTime -y 1000

# Check memory usage
./meminfo
```

### 3. Stability Monitoring
```bash
# Monitor Courant numbers
plotCourant -y 2.0  # Alert if Courant > 2.0
```

### 4. Data Transfer Between Clusters
```bash
# Copy results from Zagros
copyfromzagros simulation_results/

# Sync with cloud storage
rclone sync results/ remote:cfd-data/
```

## 🐛 Troubleshooting

### Common Issues

1. **"gnuplot not found"**
   - Activate conda environment: `conda activate gnuplot-env`
   - Install gnuplot: `conda install gnuplot`

2. **"No display available"**
   - Use PNG output: `plotKE -p`
   - Enable X11 forwarding: `ssh -X username@cluster`

3. **"Permission denied"**
   - Make scripts executable: `chmod +x script_name`

4. **"No valid points"**
   - Check data file format
   - Verify file exists and has data
   - Look for debug output messages

### Getting Help

- Check script help: `plotKE -h`
- Enable debug mode: Edit script and set `DEBUG = True`
- View error output for detailed diagnostics

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- **Hossein** - *Initial work* - [@hosseinsz93](https://github.com/hosseinsz93)

## 🙏 Acknowledgments

- Stony Brook University CEWIT
- Zagros and Seawulf HPC clusters
- CFD research community

## 📞 Support

For questions or issues:
- Open an issue on GitHub
- Contact: hossein.seyyedzadeh@stonybrook.edu

---

*Last updated: August 2025*
