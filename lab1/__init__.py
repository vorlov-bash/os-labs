from .allocator import Allocator

alloc = Allocator(70)
alloc.mem_dump()

# mem_alloc
addr1 = alloc.mem_alloc(5)
alloc.block[addr1 + 3] = 112
addr2 = alloc.mem_alloc(11)
alloc.block[addr2 + 2] = 12
addr3 = alloc.mem_alloc(8)
alloc.block[addr3 + 5] = 1
addr4 = alloc.mem_alloc(4)
alloc.block[addr4 + 3] = 121
alloc.mem_dump()

# mem_realloc
alloc.mem_realloc(addr4, 15)
alloc.mem_dump()

# mem_free
alloc.mem_free(addr1)
alloc.mem_free(addr2)
alloc.mem_free(addr3)
alloc.mem_free(addr4)
alloc.mem_dump()
