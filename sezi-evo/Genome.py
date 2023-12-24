from typing import Iterable

from Gene import Gene


class Genome():
    def __init__(self,iterable:Iterable(Gene)):
        self.__gene_list={}
        for index,gene in enumerate(iterable):self.__gene_list[f"gene-{index}"]=(gene)

    def __repr__(self) -> str:
        for gene 