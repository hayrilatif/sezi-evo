class Gene():
    def __init__(self,represantative_text:str,value):
        self.__represantative_text=represantative_text
        self.__gene_values=value
    
    def get_gene(self):
        return self.__gene_values
    
    def get_representative_text(self)->str:
        return self.__represantative_text