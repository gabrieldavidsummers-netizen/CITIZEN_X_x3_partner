import re
import base64
from io import BytesIO
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.core.clipboard import Clipboard

# ANCHORS: PILLAR 1 LOCKED
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

class PartnerEngine(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=25, spacing=15, **kwargs)
        Window.clearcolor = (0, 0, 0, 1)
        
        self.status = Label(text="[ PILLAR 1 : LOCKED ]", font_size='18sp', color=get_color_from_hex('#00ff41'), size_hint_y=0.1)
        self.add_widget(self.status)

        self.btn1 = Button(text="PUSH HERE", background_normal='', background_color=get_color_from_hex('#004400'), size_hint_y=0.15)
        self.btn1.bind(on_release=lambda x: self.strike('e'))
        self.add_widget(self.btn1)

        self.btn2 = Button(text="PUSH THIS ON NEXT", background_normal='', background_color=get_color_from_hex('#440000'), size_hint_y=0.15)
        self.btn2.bind(on_release=lambda x: self.strike('d'))
        self.add_widget(self.btn2)

        self.input = TextInput(hint_text="[SIGNAL DATA]", background_color=(0.05,0.05,0.05,1), foreground_color=(0,1,0.26,1), size_hint_y=0.3, font_size='20sp')
        self.add_widget(self.input)

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
        self.status.text = "[ COPIED ]"

class CalculatorApp(App):
    def build(self):
        self.title = "Calculator"
        return PartnerEngine()

if __name__ == '__main__':
    CalculatorApp().run()
        
