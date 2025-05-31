#!/usr/bin/env python3
"""build.py - Assembles component files into one output file based on TOC.
Source: YouBots.ai, generated with the assistance of Claude Sonnet 3.7 

2025-05-31: 
- Added one line header indicating source filename in concatendated text
- Changed .md extension to .txt for all files being searched

Usage:
    build.py <component_directory>

Example:
    build.py files-by-year

Non-License:

To the extent possible under law, the author(s) have dedicated all
copyright and related and neighboring rights to this software to the
public domain worldwide, under the CC0 terms or any more permissible
understanding of public domain. This software is distributed without
any warranty.

You can refer to the CC0 Public Domain Dedication here:
<https://creativecommons.org/publicdomain/zero/1.0/>
"""

import os
import sys
import logging
import re
from pathlib import Path


def setup_logging():
    """Configure logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    return logging.getLogger('build')


def parse_toc(toc_content):
    """
    Parse the TOC file to extract component file names.
    
    Args:
        toc_content (str): Content of the TOC file
    
    Returns:
        list: List of component file names without extension
    """
    # Skip to the first bullet list
    in_bullet_list = False
    components = []
    
    for line in toc_content.splitlines():
        line = line.strip()
        
        # Skip until we find a bullet list item
        if not in_bullet_list and line.startswith('- '):
            in_bullet_list = True
        
        # Process bullet list items
        if in_bullet_list:
            if line.startswith('- '):
                # Extract component name from the bullet item
                component = line[2:].strip()
                components.append(component)
            elif not line:
                # Empty line after bullet list - we're done
                break
            elif not line.startswith('- ') and line:
                # If we encounter a non-bullet, non-empty line after starting the list, 
                # we've reached the end of the list
                break
    
    return components


def assemble_files(component_dir, components, logger):
    """
    Read and assemble component files.
    
    Args:
        component_dir (Path): Path to the component directory
        components (list): List of component names
        logger (Logger): Logger instance
    
    Returns:
        str: Assembled content
    """
    assembled_content = []
    
    for component in components:
        # If component path contains a slash, look for it in the parent directory structure
        if '/' in component:
            # Use parent directory of component_dir as the base
            # For "common/your-job", construct path as "../common/your-job.txt"
            component_file = component_dir.parent / f"{component}.txt"
            logger.info(f"Looking for shared component: {component_file}")
        else:
            # Regular component in the specified directory
            component_file = component_dir / f"{component}.txt"
            logger.info(f"Looking for local component: {component_file}")
        
        try:
            with open(component_file, 'r', encoding='utf-8') as f:
                content = f.read()

                #2025-05-31 added source filename to top of each file
                assembled_content.append("Source Filename:") 
                assembled_content.append(f"{component_file}")
                
                assembled_content.append(content)
                logger.info(f"Added component: {component}")
        except FileNotFoundError:
            logger.error(f"Component file not found: {component_file}")
            sys.exit(1)
        except Exception as e:
            logger.error(f"Error reading component file {component_file}: {e}")
            sys.exit(1)
    
    return "\n\n".join(assembled_content)


def main():
    """Main function to handle script execution."""
    logger = setup_logging()
    
    # Check arguments
    if len(sys.argv) != 2:
        logger.error("Usage: build.py <component_directory>")
        sys.exit(1)
    
    component_dir_name = sys.argv[1]
    component_dir = Path(component_dir_name)
    
    # Check if component directory exists
    if not component_dir.is_dir():
        logger.error(f"Component directory not found: {component_dir}")
        sys.exit(1)
    
    # Read TOC file
    toc_file = component_dir / "toc.txt"
    try:
        with open(toc_file, 'r', encoding='utf-8') as f:
            toc_content = f.read()
            logger.info(f"Successfully read TOC file: {toc_file}")
    except FileNotFoundError:
        logger.error(f"TOC file not found: {toc_file}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Error reading TOC file: {e}")
        sys.exit(1)
    
    # Parse TOC to get components
    components = parse_toc(toc_content)
    
    if not components:
        logger.error("No components found in TOC file")
        sys.exit(1)
    
    logger.info(f"Found {len(components)} components to assemble")
    
    # Assemble component files
    assembled_content = assemble_files(component_dir, components, logger)
    
    # Create output directory if it doesn't exist
    output_dir = Path("../production")
    output_dir.mkdir(exist_ok=True, parents=True)
    
    # Write assembled content to output file
    output_file = output_dir / f"{component_dir_name}.txt"
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(assembled_content)
        logger.info(f"Successfully created output file: {output_file}")
    except Exception as e:
        logger.error(f"Error writing output file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
