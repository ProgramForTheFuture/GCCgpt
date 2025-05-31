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
