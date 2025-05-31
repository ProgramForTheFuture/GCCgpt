# GCCgpt
Code to automate Youtube transcript downloads for purpose of populating a custom GPT

**dlcaps.sh** is a BASH Shell script for downloading VTT transcripts for a Youtube playlist:

```
../dlcaps.sh "https://www.youtube.com/watch?v=HjChjRnz26c&list=PLOW4_Hp8_910IJ4uEe0H-oBRvSkkr1FrM"

ls *.vtt
20241103 Collaborology Study Group [3ixzr0LLk24].en.vtt
20241109 Collaborology Study Group [oWph38fLARM].en.vtt
20241110 Collaborology Study Group [Hkm_bdJ5kyA].en.vtt
20241116 Collaborology Study Group [MW8BBqlFKO4].en.vtt
20241117 Collaborology Study Group [IDs8o3yJHLY].en.vtt
20241130 Collaborology Study Group [0qJC-_Tpclg].en.vtt
20241201 Collaborology Study Group [vygR4EoEoJU].en.vtt
20241207 Collaborology Study Group [jeYeX42e2rM].en.vtt
20241208 Collaborology Study Group [ASgGYu1NLNI].en.vtt
20241214 Collaborology Study Group [a14lfAPJykE].en.vtt
20241215 Collaborology Study Group [s4VGPO_V37w].en.vtt
20241229 Collaborology Study Group [Fm1ZgISLrE0].en.vtt
20250118 Collaborology Study Group [-qTyryoRvRU].en.vtt
20250119 Collaborology Study Group [IhpYHmeQsWc].en.vtt
20250420 Heiner CSG [eEeqYq2T_pk].en.vtt
20250510 Collaborology Study Group [sSdK3w1pp3A].en.vtt
20250511 Collaborology Study Group [lxcAit6l6ng].en.vtt
20250518 Collaborology Study Group [HjChjRnz26c].en.vtt
```

**vtt_list_script.sh** creates a script to process these VTT files

```
./vtt_list_script.sh
Listing all .vtt files...
Found .vtt files, saved to vttlist.sh
Successfully added ./vtt.sh prefix and wrapped each filename in quotes in vttlist.sh

cat vttlist.sh
./vtt.sh "20241103 Collaborology Study Group [3ixzr0LLk24].en.vtt"
./vtt.sh "20241109 Collaborology Study Group [oWph38fLARM].en.vtt"
./vtt.sh "20241110 Collaborology Study Group [Hkm_bdJ5kyA].en.vtt"
./vtt.sh "20241116 Collaborology Study Group [MW8BBqlFKO4].en.vtt"
./vtt.sh "20241117 Collaborology Study Group [IDs8o3yJHLY].en.vtt"
./vtt.sh "20241130 Collaborology Study Group [0qJC-_Tpclg].en.vtt"
./vtt.sh "20241201 Collaborology Study Group [vygR4EoEoJU].en.vtt"
./vtt.sh "20241207 Collaborology Study Group [jeYeX42e2rM].en.vtt"
./vtt.sh "20241208 Collaborology Study Group [ASgGYu1NLNI].en.vtt"
./vtt.sh "20241214 Collaborology Study Group [a14lfAPJykE].en.vtt"
./vtt.sh "20241215 Collaborology Study Group [s4VGPO_V37w].en.vtt"
./vtt.sh "20241229 Collaborology Study Group [Fm1ZgISLrE0].en.vtt"
./vtt.sh "20250118 Collaborology Study Group [-qTyryoRvRU].en.vtt"
./vtt.sh "20250119 Collaborology Study Group [IhpYHmeQsWc].en.vtt"
./vtt.sh "20250420 Heiner CSG [eEeqYq2T_pk].en.vtt"
./vtt.sh "20250510 Collaborology Study Group [sSdK3w1pp3A].en.vtt"
./vtt.sh "20250511 Collaborology Study Group [lxcAit6l6ng].en.vtt"
./vtt.sh "20250518 Collaborology Study Group [HjChjRnz26c].en.vtt"
```

Execution of script:
```
./vttlist.sh
Renamed file: 20241103_Collaborology_Study_Group__3ixzr0LLk24__en
Running humantr.sh
Processing complete. Output written to 20241103_Collaborology_Study_Group__3ixzr0LLk24__en.txt
Renamed file: 20241109_Collaborology_Study_Group__oWph38fLARM__en
Running humantr.sh
Processing complete. Output written to 20241109_Collaborology_Study_Group__oWph38fLARM__en.txt
Renamed file: 20241110_Collaborology_Study_Group__Hkm_bdJ5kyA__en
Running humantr.sh
Processing complete. Output written to 20241110_Collaborology_Study_Group__Hkm_bdJ5kyA__en.txt
Renamed file: 20241116_Collaborology_Study_Group__MW8BBqlFKO4__en
Running humantr.sh
Processing complete. Output written to 20241116_Collaborology_Study_Group__MW8BBqlFKO4__en.txt
Renamed file: 20241117_Collaborology_Study_Group__IDs8o3yJHLY__en
Running humantr.sh
Processing complete. Output written to 20241117_Collaborology_Study_Group__IDs8o3yJHLY__en.txt
Renamed file: 20241130_Collaborology_Study_Group__0qJC-_Tpclg__en
Running humantr.sh
Processing complete. Output written to 20241130_Collaborology_Study_Group__0qJC-_Tpclg__en.txt
Renamed file: 20241201_Collaborology_Study_Group__vygR4EoEoJU__en
Running humantr.sh
Processing complete. Output written to 20241201_Collaborology_Study_Group__vygR4EoEoJU__en.txt
Renamed file: 20241207_Collaborology_Study_Group__jeYeX42e2rM__en
Running humantr.sh
Processing complete. Output written to 20241207_Collaborology_Study_Group__jeYeX42e2rM__en.txt
Renamed file: 20241208_Collaborology_Study_Group__ASgGYu1NLNI__en
Running humantr.sh
Processing complete. Output written to 20241208_Collaborology_Study_Group__ASgGYu1NLNI__en.txt
Renamed file: 20241214_Collaborology_Study_Group__a14lfAPJykE__en
Running humantr.sh
Processing complete. Output written to 20241214_Collaborology_Study_Group__a14lfAPJykE__en.txt
Renamed file: 20241215_Collaborology_Study_Group__s4VGPO_V37w__en
Running humantr.sh
Processing complete. Output written to 20241215_Collaborology_Study_Group__s4VGPO_V37w__en.txt
Renamed file: 20241229_Collaborology_Study_Group__Fm1ZgISLrE0__en
Running humantr.sh
Processing complete. Output written to 20241229_Collaborology_Study_Group__Fm1ZgISLrE0__en.txt
Renamed file: 20250118_Collaborology_Study_Group__-qTyryoRvRU__en
Running humantr.sh
Processing complete. Output written to 20250118_Collaborology_Study_Group__-qTyryoRvRU__en.txt
Renamed file: 20250119_Collaborology_Study_Group__IhpYHmeQsWc__en
Running humantr.sh
Processing complete. Output written to 20250119_Collaborology_Study_Group__IhpYHmeQsWc__en.txt
Renamed file: 20250420_Heiner_CSG__eEeqYq2T_pk__en
Running humantr.sh
Processing complete. Output written to 20250420_Heiner_CSG__eEeqYq2T_pk__en.txt
Renamed file: 20250510_Collaborology_Study_Group__sSdK3w1pp3A__en
Running humantr.sh
Processing complete. Output written to 20250510_Collaborology_Study_Group__sSdK3w1pp3A__en.txt
Renamed file: 20250511_Collaborology_Study_Group__lxcAit6l6ng__en
Running humantr.sh
Processing complete. Output written to 20250511_Collaborology_Study_Group__lxcAit6l6ng__en.txt
Renamed file: 20250518_Collaborology_Study_Group__HjChjRnz26c__en
Running humantr.sh
Processing complete. Output written to 20250518_Collaborology_Study_Group__HjChjRnz26c__en.txt
```

Sample transcript:
```
head 20250518*.txt

Kind: captions
Language: en
Jack, audio check. Testing, testing,
testing. I hear you. Cool.
How you been?
I just got back from Hawaii and um I I
expect full-blown jet lag shortly.
Well, so far it seems to be halfb blown.
Well, the
uh the fact that I I woke up at 6:30
```

You can then upload the transcripts into a custom GPT.

** Preparing a knowledge base to concatenate files **

The script **maketocs.sh** can be used to create toc.txt (Table of Contents) files in subdirectories under the **kb** directory containing a markdown list of all TXT files (without the extension).  This file is needed in order to use the scripts in the **bin** directory to generate files in the **production** directory.

Example:
```
./maketocs.sh
/Users/ericrangell/downloads/git/GCCgpt/kb/2020_partial
/Users/ericrangell/downloads/git/GCCgpt/kb/2021
/Users/ericrangell/downloads/git/GCCgpt/kb/2022
/Users/ericrangell/downloads/git/GCCgpt/kb/2023
/Users/ericrangell/downloads/git/GCCgpt/kb/2024
/Users/ericrangell/downloads/git/GCCgpt/kb/2025
/Users/ericrangell/downloads/git/GCCgpt/kb/before2020
```

Example toc.txt file created in before2020 subdirectory:
```
- 20120612_Collaborology_Study_Group__nF2tGrjlMPM__en
- 20160508_0603_MOAD50_DKR2__p_-sINKkR9I__ar
- 20180721_GCC_Saturday_Barn_Raising_-_Sam__Day1__86pTxtOfgZk__ar
- 20191019_GCC_Saturday_Barn_Raising__2fkDKVeKehY__ar
- 20191027_GCC_Sunday_Unblocking__jDyLS7wBWCI__ar
```

The build.sh script needs to be edited at the end to have one command for each subdirectory in the kb directory:
```
$buildcmd before2020 2> $outpath/build-before2020.txt
$buildcmd 2020_partial 2> $outpath/build-2020-partial.txt
$buildcmd 2021 2> $outpath/build-2021.txt
$buildcmd 2022 2> $outpath/build-2022.txt
$buildcmd 2023 2> $outpath/build-2023.txt
$buildcmd 2024 2> $outpath/build-2024.txt
$buildcmd 2025 2> $outpath/build-2025.txt
```

After running ./build.sh log files are created in the **bin/output** directory.  These log files should be manually reviewed, then errors should be corrected until the build runs cleanly.

Concatenated files are stored in the **production** directory.
Within each file, the source filename is printed, followed by the contents.  These files may be uploaded to a ChatGPT knowledge base.

Example:
```
production % ls -l
total 59624
-rw-r--r--  1 ericrangell  staff  2936837 May 31 09:18 2020_partial.txt
-rw-r--r--  1 ericrangell  staff  8826753 May 31 09:18 2021.txt
-rw-r--r--  1 ericrangell  staff  7339384 May 31 09:18 2022.txt
-rw-r--r--  1 ericrangell  staff  5819919 May 31 09:18 2023.txt
-rw-r--r--  1 ericrangell  staff  4427462 May 31 09:18 2024.txt
-rw-r--r--  1 ericrangell  staff   644484 May 31 09:18 2025.txt
-rw-r--r--  1 ericrangell  staff   521501 May 31 09:18 before2020.txt
```

```
head 2021.txt
Source Filename:

2021/202100828_GCC_Saturday_Barn_Raising_Foundation_Laying__Rl-LlsQFTsM__en.txt

Kind: captions
Language: en
sorry i forgot to turn on recording
i mean mostly i listened to music when i
was much younger not so much anymore
but i always loved uh john baez he's not
```

Note: Scripts and Python code were created with the assistance of Claude Sonnet

