from typing import Iterable

from Gene import Gene


class Genome():
    def __init__(self,iterable:Iterable(Gene)):
        self.__gene_dict={}
        for index,gene in enumerate(iterable):self.__gene_dict[f"gene-{index}"]=(gene)
    def __repr__(self) -> str:
        for gene_key in self.__gene_dict.keys():
            gene=self.__gene_dict.get(gene_key)
            
            print("GeneTypeObject")
            print("*")
            print(f"***{gene_key}***")
            print("*")
            print(f"Representative: {gene.get_representative_text()}")
            print("*")
            print(f"Values: {gene.get_gene()}")

    