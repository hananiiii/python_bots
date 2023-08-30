import random

R_EATING='i dont like that dish'
def unknown():
    response=['could you please re-phrase that?',"..."
              ,"sounds about right","what does that mean"][random.randrange(4)]

    return response
    