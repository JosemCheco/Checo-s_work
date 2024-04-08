import flet as ft
import random

def main(page: ft.Page):
    def rollDice(e):
        valor = random.randint(1, 6)
        rollnumber.value = str(valor)
        
        if valor == 1:
            dicephoto.src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjmZnLKLmHDi8MUrDZHxKxForoTvpBAnx-8g&usqp=CAU"
        elif valor == 2:
            dicephoto.src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhHCgZTdveUb-HlPA01nb-oSWu9V0Xbt4DxWNwqjDywhixgqlEOIqG7Glh6-2AYcTQHT4&usqp=CAU"
        elif valor == 3:
            dicephoto.src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_EADJgk-v2tk34Vt1rVpsyY-zBueq74nPAGJd_I3mmi8oZCJoOYPqzlH4P_IXh1k9wIw&usqp=CAU"
        elif valor == 4:
            dicephoto.src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCFHsBM5ASpn9zAwvNFBsGiEiwxctFTGnk-hPmOdhvX0qei53nAqmbH4Nf2Iv-piRvkeQ&usqp=CAU"
        elif valor == 5:
            dicephoto.src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTu2qZ--xtRQ_8ZPmagZKoio3qkjcubXR7Nmj3DDE4jIFVJnuiL9gGdNgpNjV_Dufdv89k&usqp=CAU"
        elif valor == 6:
            dicephoto.src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzUosrdJmBo3LMMw7foSJ6E5DVd6uSCKEILw&usqp=CAU"
        page.update()

    page.horizontal_alignment = "CENTER" 
    page.vertical_alignment = "CENTER" 

    dicephoto = ft.Image(src="genericDice.png") 
    rollnumber = ft.Text(value="ROLL THE DICE NOW", size=40)
    randombutton = ft.ElevatedButton(text="Roll Dice again and then again", height=30, width=300, on_click=rollDice)
    page.add(dicephoto, rollnumber, randombutton)

ft.app(target=main)