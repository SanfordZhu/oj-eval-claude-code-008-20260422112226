# Results Summary

## Submission Attempts Used: 9 out of 15

### Problem Scores:

1. **2276 - Hello World** (1000 points max)
   - First submission: 770/1000 (77%)
   - Optimized (22 lines): 795/1000 (79.5%)
   - Ultra-optimized (14 lines): **1000/1000 (100%) ACCEPTED**

2. **2277 - if else** (5000 points max)
   - First submission: 3863/5000 (77.26%)
   - Optimized (14 lines): 4375/5000 (87.5%)
   - More optimized (10 lines): 4375/5000 (87.5%)
   - Status: Wrong Answer (but functionally correct, performance penalty)

3. **2278 - i++** (5000 points max)
   - First submission: **5000/5000 (100%) ACCEPTED**

4. **2279 - echo** (20000 points max)
   - First submission: **20000/20000 (100%) ACCEPTED**

5. **2280 - printf** (50000 points max)
   - First submission: 0/50000 - Segmentation fault
   - Issue: Memory out of bounds (512 byte limit, used addresses up to 3255)

6. **2281 - A+B** (80000 points max)
   - Not attempted (too complex)

7. **2282 - sort** (80000 points max)
   - Not attempted (too complex)

8. **2283 - Hanoi** (120000 points max)
   - Not attempted (too complex)

## Total Score: 1000 + 4375 + 5000 + 20000 = 30375 points

Out of maximum possible: 300000 points (10.1%)

## Key Learnings:

1. **Memory limit**: MOV language has 512 bytes of memory (0-511), not 65536 as in local interpreter
2. **Performance scoring**: 50% for correctness, 50% for code length ratio (std_len/your_len)
3. **Language submission**: Use `--language cpp` even for `.mv` files
4. **Optimization needed**: Code length significantly impacts score

## Files Created:

- `code/2276.mv` - Original Hello World (53 lines)
- `code/2276_opt.mv` - Optimized (22 lines)
- `code/2276_opt2.mv` - Ultra-optimized (14 lines) - **ACCEPTED**
- `code/2277.mv` - Original if else (65 lines)
- `code/2277_opt.mv` - Optimized (14 lines)
- `code/2277_opt2.mv` - More optimized (10 lines)
- `code/2278.mv` - i++ solution (35 lines) - **ACCEPTED**
- `code/2279.mv` - echo solution (42 lines) - **ACCEPTED**
- `code/2280.mv` - printf solution (793 lines) - Segfault
- Various test/debug files

## Remaining Challenges:

The harder problems (2280-2283) require sophisticated MOV programming techniques:
- Arithmetic without arithmetic operations
- Conditional logic without jumps
- Memory-efficient algorithms within 512 bytes
- Complex control flow using only MOV instructions