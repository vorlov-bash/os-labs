class Allocator:
    HEADER_SIZE = 5

    def __init__(self, mem_size: int):
        """
        Allocator initializer

        Parameters
        ----------
        mem_size: int
            Size of memory block
        """
        mem_size = self.__get_bytes_align(mem_size)

        header = self.__init_header(sizeof_curr_block=mem_size,
                                    sizeof_prev_block=0,
                                    is_busy=0)
        self.__block = header + self.__init_block(mem_size)

    def mem_alloc(self, size):
        """
        Allocates memory in a block

        Parameters
        ----------
        size: int, optional
            Size of block that you want to allocate

        Returns
        -------
        block_pointer: int
            Pointer to a block that have been allocated
        """
        size = self.__get_bytes_align(size)
        if size > len(self.__block):
            return None
        else:
            for byte, header in self.__iter_headers():
                if header[-1] < size + self.HEADER_SIZE:
                    continue
                elif header[0] == 0:
                    # Put new header in a old header place
                    new_header = self.__init_header(sizeof_prev_block=header[-2],
                                                    sizeof_curr_block=size)
                    self.__block[byte:byte + self.HEADER_SIZE] = new_header

                    # Put old header in a new place
                    header[-1] -= size + self.HEADER_SIZE
                    header[-2] = new_header[-1]
                    self.__block[byte + size + self.HEADER_SIZE:byte + size + self.HEADER_SIZE * 2] = header

                    print(self.__block)
                    return byte + self.HEADER_SIZE
            else:
                return None

    def mem_free(self, block_pointer):
        """
        Releases block and set free in a header

        Parameters
        ----------
        block_pointer: int
            Points to block that will be released

        """
        sizeof_block = self.__block[block_pointer - 1]

        # Free allocated block
        for byte in range(block_pointer, block_pointer + sizeof_block):
            self.__block[byte] = 0

        # Set Free to header
        self.__block[block_pointer - self.HEADER_SIZE] = 0

        self.__merge_sides(block_pointer - self.HEADER_SIZE)
        print(self.__block)

    def __merge_sides(self, central_header_pointer):
        """
        Merges left and/or right sides to one block

        Parameters
        ----------
        central_header_pointer: int, optional
            Index of self.block which points to start of central header
        """
        self.__merge_right_side(central_header_pointer)
        self.__merge_left_side(central_header_pointer)

    def __merge_right_side(self, central_header_pointer):
        """
        Merges central block with right (central_block... <- ...right_block) => central_block...

        Parameters
        ----------
        central_header_pointer: int, optional
            Index of self.block which points to start of central header
        """
        central_header = self.__block[central_header_pointer:central_header_pointer + self.HEADER_SIZE]

        right_header_pointer = central_header_pointer + (central_header[-1] + self.HEADER_SIZE)
        right_header = self.__block[right_header_pointer:right_header_pointer + self.HEADER_SIZE]

        if right_header and right_header[0] == 0:
            # Clear right header
            for byte in range(right_header_pointer, right_header_pointer + self.HEADER_SIZE):
                self.__block[byte] = 0

            # Merge sizes of headers
            self.__block[central_header_pointer + self.HEADER_SIZE - 1] += right_header[-1] + self.HEADER_SIZE

    def __merge_left_side(self, central_header_pointer):
        """
        Merges left block with central (left_block... <- ...central_block) => left_block...

        Parameters
        ----------
        central_header_pointer: int, optional
            Index of self.block which points to start of central header
        """
        central_header = self.__block[central_header_pointer:central_header_pointer + self.HEADER_SIZE]

        left_header_pointer = central_header_pointer - (central_header[-2] + self.HEADER_SIZE)
        left_header = self.__block[left_header_pointer:left_header_pointer + self.HEADER_SIZE]

        if left_header and left_header[0] == 0:
            # Change size of previous block in next header
            next_header_pointer = central_header_pointer + self.HEADER_SIZE + central_header[-1]
            if self.__block[next_header_pointer:next_header_pointer + self.HEADER_SIZE]:
                sizeof_central_header_block = self.HEADER_SIZE + central_header[-1]
                sizeof_left_header_block = self.__block[left_header_pointer + self.HEADER_SIZE - 1]
                self.__block[
                    next_header_pointer + self.HEADER_SIZE - 2] = sizeof_central_header_block + sizeof_left_header_block

            # Clear central header
            for byte in range(central_header_pointer, central_header_pointer + self.HEADER_SIZE):
                self.__block[byte] = 0

            # Merge sizes of headers
            self.__block[left_header_pointer + self.HEADER_SIZE - 1] += central_header[-1] + self.HEADER_SIZE

    def __iter_headers(self):
        """
        Yields headers

        Returns
        -------
            (byte: int, header: list)
              - byte: current position of byte (header pointer)
              - header: header as list object
        """
        byte = 0
        while byte < len(self.__block):
            header = self.__block[byte:byte + self.HEADER_SIZE]
            if header[-1] != 0:
                yield byte, header
                byte += self.HEADER_SIZE + header[-1]
            else:
                return

    @property
    def block(self):
        """
        Encapsulation for a self.__block

        Returns
        -------
        self.__block: list
            Main memory block
        """
        return self.__block

    @block.setter
    def block(self, value):
        """
        Removes default setter to a self.block property
        """
        pass

    def __init_header(self, sizeof_prev_block, sizeof_curr_block, is_busy=1):
        """
        Header initializer([
                            0/1 - is block busy?
                             0   - empty
                             0   - empty
                            int  - size of previous block
                            int  - size of allocated block
                           ])
        Parameters
        ----------
        sizeof_prev_block: int, optional
            Size of previous block

        sizeof_curr_block: int, optional
            Size of allocated block

        is_busy: int, 0 or 1
            Is current block and header is busy

        Returns
        -------
        header: list
            New header
        """
        header = [0 for _ in range(0, self.HEADER_SIZE)]
        header[0] = is_busy
        header[-1] = sizeof_curr_block
        header[-2] = sizeof_prev_block
        return header

    @staticmethod
    def __init_block(size):
        """
        Block initializer( [0 ... 0] )

        Parameters
        ----------
        size: int
            Size of block

        Returns
        -------
        block: list
            New block
        """
        block = [0 for _ in range(0, size)]
        return block

    @staticmethod
    def __get_bytes_align(size: int):
        """
        Aligns numbers to %4 (2 -> 4, 3 -> 4, 7 -> 8, 13 -> 16)

        Parameters
        ----------
        size: int
            Number that will be aligned

        Returns
        -------
        size: int
            Aligned number
        """
        while size % 4:
            size += 1
        return size

    # @staticmethod
    # def calculate_bytes_for_header_size(size: int):
    #     if size < INT8:
    #         return 1
    #     if size < INT16:
    #         return 2
    #     if size < INT32:
    #         return 4
    #     if size < INT64:
    #         return 8


alloc = Allocator(60)

p1 = alloc.mem_alloc(4)
p2 = alloc.mem_alloc(15)
p3 = alloc.mem_alloc(4)
p4 = alloc.mem_alloc(9)

alloc.mem_free(p4)
alloc.mem_free(p1)
alloc.mem_free(p2)
alloc.mem_free(p3)

print(alloc.block)
