class Genome():
    def __init__(self,iterable):
        self.__gene_list={}
        for index,gene in enumerate(iterable):self.__gene_list[f"gene-{index}"]=(gene)