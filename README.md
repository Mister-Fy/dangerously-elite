# dangerously-elite
It started as somewhere to share Elite:Dangerous tools. 
The first one, HGE Hunter, is my first ever Python code and it scrapes a JSON file on EDDB to help identify star systems which could/should yield specific high-grade manufactured materials which are used to engineer ships' modules and weapons. It is important to note that in the game, some systems can exhibit multiple states simultaneously.

The HGE materials and their corresponding system states are as follows:
```
1: Core Dynamics Composites - Federation systems which are not in Boom, Outbreak, Civil War, War or Civil Unrest states
2: Imperial Shielding - Imperial systems which are not in Boom, Outbreak, Civil War, War or Civil Unrest states
3: Improvised Components - Independant systems which are in Civil Unrest, but not in Boom, Outbreak, Civil War or War states
4: Military Grade Alloys/Supercapacitors - Independant systems which are in Civil War or War, but not in Boom, Outbreak or Civil Unrest states
5: Pharmaceutical Isolators - Independant systems which are in Outbreak, but not in Boom, Civil War, War or Civil Unrest states
6: Proto Heat Radiators/Radiolic Alloys - Independant systems which are in Boom, but not in Outbreak, Civil War, War or Civil Unrest states```
