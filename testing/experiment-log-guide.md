# Experiment log guide

- Each row summarizes one agent version against one opponent, for one seed set and one seat.
- For paired autoplay tests, make two rows, one for P1 and one for P2.
- To compare versions fairly, use the same opponent, seeds, and setup.
- The simulator can save game details with `--json testing\<run-name>.jsonl`. Use a new filename for each run. 
- The console shows overall results and timing, while the JSON file has per-game details.
- Leave unavailable fields blank or write `N/A`. Never enter zero for a value that was not measured.

| Field | What to enter |
|---|---|
| `date_local` | Date of the test, in `YYYY-MM-DD` format. |
| `commit` | Git commit for the tested code. Find it in Source Control or run `git rev-parse --short HEAD`. |
| `agent_version` | Short label for the build, like `starter-random`, `v1`, or `v2`. Use the same label for both seat rows. |
| `change_summary` | What changed in this version. For the starter, write that it uses random moves. |
| `opponent` | Opponent name from the command, like `random_agent` or `greedy_agent`. |
| `seed_or_seed_range` | Seed from `--seed` or the seed range printed by autoplay. Each pair uses one seed. |
| `obstacle` | Obstacle location, like `1,2`. Find it in the JSON `obstacle` field. Write `mixed` if the seed set has several locations. |
| `removed_piece` | Removed size, `S`, `M`, or `L`. In JSON, `removed_size` is 0 for small, 1 for medium, and 2 for large. Write `mixed` if the seed set has several sizes. |
| `game_pairs` | Number of seat-swapped pairs. This is half of `--autoplay_runs` and appears in the console summary. |
| `agent_seat` | `P1` or `P2`. Make a separate row for each seat. |
| `wins`, `draws`, `losses` | Results for the agent in this seat. Use the JSON `players` and `winner` fields. A winner value of 0 means a draw. |
| `mean_move_ms` | Average move time in milliseconds. JSON stores `agent_time` in seconds. Multiply by 1000 to convert it. |
| `max_move_ms` | Longest move time in milliseconds. Use JSON for a seat-specific value. The console summary combines both seats. |
| `strikes` | Strike count for this seat, from the JSON `strikes` field or the console summary. |
| `forfeits` | Number of games the agent forfeited in this seat. Check the JSON `reason` field for reasons like `hard_timeout`, `crash`, or `too_many_strikes`. |
| `strict_mode` | `true` if the command used `--strict`, otherwise `false`. Note platform warnings in `notes`. |
| `command` | Full command used for the test. |
| `raw_jsonl_path` | Path to the JSON file, or blank if you did not save one. |
| `notes` | Warnings, incomplete runs, or anything else needed to understand the results. |

- Each row covers one seat across the listed pairs.
- If a run stops early, record the completed pairs and explain why in `notes`.
- Keep different opponents or seed sets in separate rows.
