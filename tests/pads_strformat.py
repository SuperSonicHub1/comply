# Equivalent to: 
#  nullsrc, split[L1], [L1]overlay, nullsink
#  nullsrc, split[L2], [L2]overlay, nullsink

for i in range(1, 3):
	nullsrc() | split() >> {f"L{i}"} | {f"L{i}"} >> overlay() | nullsink()
