from yoomoney import Quickpay
quickpay = Quickpay(
            receiver="41001671667170",
            quickpay_form="shop",
            targets="Sponsor this project",
            paymentType="SB",
            sum=95,
            label="55"
            )
print(quickpay.base_url)
print(quickpay.redirected_url)