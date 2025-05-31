#/bin/bash
# Build script for knowledge base for GCC
# Run this script from the bin directory

current_dir="$PWD"
if [[ "$current_dir" != */bin ]]; then
    echo "Error: Script must be run from 'bin' directory" >&2
    exit 1
fi

agentdir="../kb"
outdir="output"
outpath="../bin/$outdir"
proddir="../production"
buildcmd="../bin/build.py"

if [ ! -d $outdir ]
then
  mkdir -p $outdir
fi
if [ ! -d $proddir ]
then
  mkdir -p $proddir
fi

cd $agentdir
$buildcmd before2020 2> $outpath/build-before2020.txt
$buildcmd 2020_partial 2> $outpath/build-2020-partial.txt
$buildcmd 2021 2> $outpath/build-2021.txt
$buildcmd 2022 2> $outpath/build-2022.txt
$buildcmd 2023 2> $outpath/build-2023.txt
$buildcmd 2024 2> $outpath/build-2024.txt
$buildcmd 2025 2> $outpath/build-2025.txt

