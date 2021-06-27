import justpy as jp

class About:
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, text= "This is the About page!", classes="text-4xl m-2")
        div = jp.Div(a=wp, text="""
        A photos collection and NLP material search       
        """, classes="text-lg")
        div = jp.Div(a=wp, text= "this are stefano's media", classes="bg-gray-200 h-screen")
        return wp

