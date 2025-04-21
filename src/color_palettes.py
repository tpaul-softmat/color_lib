#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 16:00:02 2025

@author: tanay; Help: ChatGPT
"""

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from matplotlib import colormaps

def get_palette_colors(palette_name, n_colors=256, vmin=None, vmax=None, min_frac=0.2, max_frac=0.8):
    """
    Returns a list of color hex codes from a specified portion of the given colormap, 
    mapping vmin and vmax to the extremes of the selected range.

    Parameters:
        palette_name (str): Name of the colormap (e.g., 'viridis', 'plasma').
        n_colors (int): Number of colors to extract (<=256 for the best performance; default: 256).
        vmin (float, optional): Minimum value for normalization.
        vmax (float, optional): Maximum value for normalization.
        min_frac (float, optional): Lower bound of the colormap fraction (default: 0.2).
        max_frac (float, optional): Upper bound of the colormap fraction (default: 0.8).

    Returns:
        List of hex color codes.
    """
    if palette_name not in plt.colormaps():
        raise ValueError(f"Unknown palette '{palette_name}'. Choose from {plt.colormaps()}")

    cmap = colormaps.get_cmap(palette_name)

    # Set default vmin and vmax
    if vmin is None:
        vmin = 0
    if vmax is None:
        vmax = n_colors - 1

    # Normalize vmin and vmax within [0,1]
    norm = mcolors.Normalize(vmin=vmin, vmax=vmax)
    normalized_values = norm(np.linspace(vmin, vmax, n_colors))  # Normalized within [0,1]

    # Scale normalized values to fit within [min_frac, max_frac]
    scaled_values = min_frac + (max_frac - min_frac) * normalized_values

    # Extract colors from the scaled portion of the colormap
    colors = [mcolors.to_hex(cmap(v)) for v in scaled_values]

    return colors

# Predefined palettes
colormapnames = list(colormaps)
PALETTES = {
    item : get_palette_colors(palette_name=item) for item in colormapnames
    # "viridis": get_palette_colors(palette_name="viridis"),
}

def get_palette(name):
    """Retrieve predefined color palette as a list of hex codes."""
    return PALETTES.get(name, f"Palette '{name}' not found.")
