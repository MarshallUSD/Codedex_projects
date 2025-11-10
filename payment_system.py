# Goal : show polymorhism in action
"""""
from abc import ABC, abstractmethod

class PayProcessor(ABC):
    @abstractmethod
    def process(self, ammount):
        
        pass
     
     # implement:paypal , card, crypto

class PayPalProocessor(PayProcessor):
    def process(self, ammount):
        print(f"Processing payment of {ammount} using PayPal.")


class CardProcessor(PayProcessor):
    def process(self, ammount):
        print(f"Processing payment of {ammount} using Credit/Debit Card.")

class CryptoProcessor(PayProcessor):    
    def process(self, ammount):
        print(f"Processing payment of {ammount} using Cryptocurrency.")

        


def process_payment(processor: PayProcessor, ammount):
    processor.process(ammount)                                                              
paypal_processor = PayPalProocessor()
card_processor = CardProcessor()    
crypto_processor = CryptoProcessor()
process_payment(paypal_processor, 100)
process_payment(card_processor, 250)
process_payment(crypto_processor, 500)


"""

#media player
# subclasses: mp3, mp4, wav
#loop over files and play them

from abc import ABC, abstractmethod

class MediaPlayer(ABC):
    @abstractmethod
    def play(self, filename):
        pass

class MP3Player(MediaPlayer):
    def play(self, filename):
        print(f"Playing MP3 file: {filename}")
class MP4Player(MediaPlayer):
    def play(self, filename):
        print(f"Playing MP4 file: {filename}")
class WAVPlayer(MediaPlayer):
    def play(self, filename):
        print(f"Playing WAV file: {filename}")
def play_media(player: MediaPlayer, filename):
    player.play(filename)           
mp3_player = MP3Player()
mp4_player = MP4Player()        
wav_player = WAVPlayer()
play_media(mp3_player, "song.mp3")
play_media(mp4_player, "video.mp4") 
play_media(wav_player, "audio.wav")

