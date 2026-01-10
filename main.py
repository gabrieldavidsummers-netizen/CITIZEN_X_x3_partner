import re
import base64
from io import BytesIO
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image as KivyImage
from kivy.core.image import Image as CoreImage
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.core.clipboard import Clipboard

# ANCHORS: PILLAR 1 LOCKED
SIG = "13579"
PILLAR_VALUE = 609
LEXICON = {
    "corpus": "445¹⁶", "attachment": "7o⁷⁷9", "characterization": "9⁴⁹31", 
    "adopted": "⁷⁹³85", "skilled": "¹5³92", "guns": "88⁶⁶⁹", 
    "operators": "603³⁷", "obtaining": "⁶56O8", "formula": "94²⁶⁶", 
    "lycos": "⁵1o⁸3", "gi": "³416²", "sister": "8⁵³8³", "aaa": "¹⁷83⁸",
    "federal": "29⁷38", "milfhunter": "39⁸⁹3", "students": "6³³¹²", 
    "ceremony": "15⁶9⁷", "books": "268⁹2", "transformation": "6⁵6⁰1", 
    "collector": "12938", "european": "²⁶⁰⁹7", "jazz": "⁴⁵⁶25", 
    "pushed": "8⁴⁵5⁹", "domain": "8⁴²13", "diseases": "⁷2³63", 
    "highways": "⁶88²⁶"
}
REVERSE_LEXICON = {v: k for k, v in LEXICON.items()}
ICON_DATA = "iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAYAAABw4pVUAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAJVSURBVHgB7Z27TsMwFIY7S6XpA6BeAs9ReAZewYpX6EwMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTEz8V2qS7+RL7HhOnGPrL2ma/mDq9Xp7ruueHId83/8aj8dfY7HYeS6XayQSidTZbPa1v7//6TzW6XS+mqY59TzfOvX9+v6Sruuvm83mZ7Va/R6PxyeO9Xy9Xv8sl8tPmqZ979T36/tLmqZfs9nsR6FQ+OYYP7X7fD7/WywWv7vdbuvU9+v7S5qmX6vV6mcyY9mNf9/vVygUPm9vbw/Y9+v7S5qmX6vV6mc6nd5ixv6uUCis2+32XmPfr+8vaZp+rVarX9ls9pMZG+wWi8VuOByuNfb9+v6Sput3OBz29vv93mw2+8WMTfbhcLjt9/u/Gvt+fX9J0/W73W7vPB7fo9HozYxN9oPB4O3S2Pfr+0uapv/7B0Y0Gr1gxqb7fr//fGns+/X9JU3TX7/f7zO9/KXT6Sxm9E99v76/pGn6P5/P78mP7Ha7u8zo9/r9/vOts+/X95c0Tf/X6/V9v9/fkB/L7v/P7Pe63e7LrbPv1/eXNE3/l8vlfbfb3ZIf6+7/T/v9/vO9Y9+v7y9pmn4tl8v7brfbkx/r7v9P+/3+86Nj36/vL2mafi2Xy/vj8fgWM/Z3lUrl6/X19R77fn1/SdP0fzwe32LHc+I8X39R1Wp1v9Vq7Tr1/fr+kqbpX6/X99jxnDjf9yWRSNReXFycOPX9+v6SpukXf6p0Oh3/Y/kK69T36/v7B5Z6eV3A8MclAAAAAElFTkSuQmCC"

class PartnerEngine(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=25, spacing=15, **kwargs)
        Window.clearcolor = (0, 0, 0, 1)
        img_data = BytesIO(base64.b64decode(ICON_DATA))
        self.add_widget(KivyImage(texture=CoreImage(img_data, ext='png').texture, size_hint_y=0.2))
        
        # STATUS DISPLAY
        self.status = Label(text="[ PILLAR 1 : LOCKED ]", font_size='18sp', color=get_color_from_hex('#00ff41'), size_hint_y=0.1)
        self.add_widget(self.status)

        # BUTTON 1: PUSH HERE (ENCRYPT)
        self.btn1 = Button(text="PUSH HERE", background_normal='', background_color=get_color_from_hex('#004400'), size_hint_y=0.15)
        self.btn1.bind(on_release=lambda x: self.strike('e'))
        self.add_widget(self.btn1)

        # BUTTON 2: PUSH THIS ON NEXT (DECRYPT)
        self.btn2 = Button(text="PUSH THIS ON NEXT", background_normal='', background_color=get_color_from_hex('#440000'), size_hint_y=0.15)
        self.btn2.bind(on_release=lambda x: self.strike('d'))
        self.add_widget(self.btn2)

        # INPUT/OUTPUT AREA
        self.input = TextInput(hint_text="[SIGNAL DATA]", background_color=(0.05,0.05,0.05,1), foreground_color=(0,1,0.26,1), size_hint_y=0.3, font_size='20sp')
        self.add_widget(self.input)

        # BUTTON 3: THIS IS THE THIRD BUTTON (COPY)
        self.btn3 = Button(text="THIS IS THE THIRD BUTTON", size_hint_y=0.1, background_color=get_color_from_hex('#000044'))
        self.btn3.bind(on_release=self.copy_out)
        self.add_widget(self.btn3)

    def strike(self, m):
        t = self.input.text.strip().lower()
        if not t: return
        if m == 'e':
            w = re.findall(r'\b[a-z0-9]+\b', t)
            result = " ".join([LEXICON.get(i, f"[{i}]") for i in w])
        else:
            result = " ".join([REVERSE_LEXICON.get(i, "[?]") for i in t.split()])
        self.input.text = result
        self.status.text = f"[ SIGNAL {'PROCESSED' if m == 'e' else 'DECODED'} ]"

    def copy_out(self, i):
        Clipboard.copy(self.input.text)
        self.status.text = "[ COPIED TO SYSTEM BUS ]"

class PartnerApp(App):
    def build(self):
        self.title = "PARTNER_X"
        return PartnerEngine()

if __name__ == '__main__': PartnerApp().run()
