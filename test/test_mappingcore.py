import unittest
import os.path
#import fastqori.mappingcore
from fastqori import mappingcore


class TestMappingCore(unittest.TestCase):
    """Testing function of fastqori The fastq data are coming from
    bosTaurusUMD3, oviAriOar4, capHirARS1 and homSapGRCh38

    and were generated with wgsim:

    wgsim -N 100 -r 0.01 -1 50 -S11 -d0 -e0 bosTaurusUMD3.1.1.fasta \
    bosTaurusUMD3.1.1.fastq /dev/null

    wgsim -N 10 -r 0.01 -1 50 -S11 -d0 -e0 oviAriOar4.fasta \
    oviAriOar4.fastq /dev/null

    wgsim -N 20 -r 0.01 -1 50 -S11 -d0 -e0 capHirARS1.fasta \
    capHirARS1.fastq /dev/null

    wgsim -N 20 -r 0.01 -1 50 -S11 -d0 -e0 homSapGRCh38.fasta \
    homSapGRCh38.fastq /dev/null

    cat *.fastq > read_pool.fastq
    We added some reads of the parchment

    head -n 100 ../../../parchment/finalReads/reads_ATTCAGAA.fastq >\
    parchment.fastq

    The fasta data are from the same genome we used to generate the reads.

    """
    # dummy test
    def test_dummy(self):
        self.assertEqual(1, 1)
        
    def setUp(self):
        pass

    def test_indexing_bwa(self):
        # generate bwa index
        mappingcore.generateindex("./test/test.fasta", "bwa index")
        # check that index is present
        self.assertTrue(os.path.exists("./test/test.fasta.sa"))

    def test_mapping_bwa(self):
        # mapping reads
        mappingcore.mapreads("./test/test.fasta",
                             "./test/read_pool.fastq", "bwa mem")
        self.assertTrue(os.path.exists("./test/read_pool.fastq.sam"))


if __name__ == '__main__':
    unittest.main()
