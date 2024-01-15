###Izveidot Python programmu, kas nolasītu un izdrukātu visu teksta faila saturu (txt formātā) 
 
def izlaist_teksta_failu(PD)  
     with open(PD, 'r') as faila: 
         faila_saturs= PD.read() 
     print(faila_saturs) 
     faila_nosaukums=input('ievadiet faila nosaukumu ar teksta paplašinājumu') 
     izlaist_teksta_failu(faila_nosaukums)
      
     