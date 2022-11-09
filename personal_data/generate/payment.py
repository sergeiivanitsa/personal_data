from yoomoney import Quickpay, Client



def paylink(id):

	#token = "41001671667170.275356671D62ABAE304CC1E61E83C7E6F53D48AC4EBD8798EFA43796D6399677F7CD37D68EF4EDC7C92814C7A254CE4451F1088C77E51FB05A877E019A2A7C0843CFC777A81BF6978F06AFFE65CE56CF8165147F139C0AE6B6C39BB135EAA8FDC36B30CED87938852D7AA92BF8040970A6B809AE6C90C8E7BECCB99BE7600AB7"
	#client = Client(token)
	#user = client.account_info()

	quickpay = Quickpay(receiver="41001671667170",
            			quickpay_form="shop",
            			targets="Sponsor this project",
            			paymentType="SB",
            			sum=95,
            			label=f"{id}")
	return(quickpay.base_url)
	#return(quickpay.redirected_url)