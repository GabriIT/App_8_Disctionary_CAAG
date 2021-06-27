import justpy as jp

class Home:
    path = "/"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, text="This is the HOME page!", classes="text-4xl m-2")
        div = jp.Div(a=wp, text="""
        A photos collection and NLP material search        

        """, classes="text-lg")
        div = jp.Div(a=wp, text="this are stefano's media", classes="bg-gray-200 h-screen")
        return wp


