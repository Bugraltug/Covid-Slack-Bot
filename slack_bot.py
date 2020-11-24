class SlackBot: 

    Main_Block = {
         "type": "section",
         "text": { "type": "mrkdwn", "text": ( "Text...\n\n" ), }, 
        } 
    
    def __init__(self, channel): 
        self.channel = channel 
    
    def _additional_block(self):
        text = "Text 2" 
        return {
            "type": "section", 
            "text": {"type": "mrkdwn", "text": text}}
        
    def get_message_payload(self): 
        return { 
            "channel": self.channel, 
            "blocks": [self.Main_Block, *self._additional_block(),], 
        }
