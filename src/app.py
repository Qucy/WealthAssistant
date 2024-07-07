import gradio as gr
from load_image import image_to_numpy_array


# load avatars
rm_avatar_jpg = image_to_numpy_array("C:\\Users\\tracy\\Downloads\\1718919859070.jpg")
# loading clinet avatars
client_avatar = image_to_numpy_array("C:\\Users\\tracy\\Downloads\\1718919859070.jpg")


def mock_up_clients():
    """ return mockup clients in JSON Array Format with keys
    - id
    - name
    - segement
    - investment_persona
    - tcr
    - profofile
    - avatar
    """
    return [
        {
            "id": "1",
            "name": "Jason Bourne",
            "segment": "Premium",
            "investment_persona": "Buy and Hold",
            "tcr": "100000",
            "profile": "200000",
            "avatar": ""
        },
        {
            "id": "2",
            "name": "James Bonds",
            "segment": "Premium Lite",
            "investment_persona": "Advisory",
            "tcr": "300000",
            "profile": "200000",
        },
        {
            "id": "3",
            "name": "Lucy Liu",
            "segment": "Premium",
            "investment_persona": "Buy and Hold",
            "tcr": "100000",
            "profile": "200000",
        },
        {
            "id": "4",
            "name": "Mike Tyson",
            "segment": "Premium",
            "investment_persona": "Buy and Hold",
            "tcr": "100000",
            "profile": "200000",
        },
        {
            "id": "5",
            "name": "Daniel Craig",
            "segment": "Premium",
            "investment_persona": "Advisory",
            "tcr": "100000",
            "profile": "200000",
        }
    ]


def update_customer_profile(client_id):
    """ return customer profile, finicial news and talking points """
    client = [client for client in clients if client["id"] == client_id][0]
    client_name = client["name"]
    client_investment_persona = client["investment_persona"]
    client_segment = client["segment"]
    client_tcr = client["tcr"]
    return client_segment, client_investment_persona, client_tcr, client, "finicial news", "talking points"

# retrieve clients
clients = mock_up_clients()

# Extracting a list of client names for the choices
client_dropdowns = [(client['name'], client['id']) for client in clients]

with gr.Blocks() as RMAssistant:
    # Title
    gr.Markdown("## Wealth Assistant PoC")
    # ====================================== Customer tab to display RM basic info and customer list ======================================
    with gr.Tab('Customers'):
        with gr.Row():
            # column to display RM basic information
            with gr.Column(
                scale=1, 
                variant="compact", 
                min_width=200
            ):
                # RM avatar
                rm_avatar = gr.Image(
                    label='John Doe',
                    value=rm_avatar_jpg,
                )
                # RM ID
                gr.Text(
                    label="Staff ID",
                    value="450DB8921",
                )
                # RM Name
                gr.Text(
                    label="Staff Name",
                    value="John Doe",
                )
                # RM Branch
                gr.Text(
                    label="Staff Branch",
                    value="Causeway Bay HK",
                )
                # RM Title
                gr.Text(
                    label="Staff Title",
                    value="Senior Relationship Manager",
                )

            # column to display RM's clients
            with gr.Column(
                scale=2, 
                variant="compact"
            ):  
                for client in clients:
                    # RM's clients
                    with gr.Row():
                        # Clients Name
                        c_name = gr.Text(
                            label="Name",
                            value=client["name"],
                        )
                        # Client Segement - Premium or Premium Lite
                        gr.Text(
                            label="Segment",
                            value=client["segment"],
                        )
                        # Client Investment Personal - Buy and hold or Advisory
                        gr.Text(
                        label="Investment Personal", 
                        value=client["investment_persona"],
                        )
                        # Client TCR
                        gr.Text(
                            label="TCR",
                            value=client["tcr"],
                        )                  

    # ====================================== Customer tab to display customer profiling info  ======================================
    with gr.Tab("Customer Profiling"):
        # column to display RM's clients
        cust_select = gr.Dropdown(
            label="Select Client",
            choices=client_dropdowns,
        )
        with gr.Row():  
            # Customers
            with gr.Column(
                scale=1, 
                variant="compact", 
                min_width=200
            ):
                # Customer avatar
                cust_avatar = gr.Image(
                    label="Customer Avatar",
                    value=rm_avatar_jpg,
                )
                # Customer Segment - Premium or Premium Lite
                cust_seg_text = gr.Text(
                    label="Segment",
                    value="",
                )
                # Customer Investment Personal - Buy and hold or Advisory
                cust_invst_personal_txt = gr.Text(
                    label="Investment Personal",
                    value="",
                )
                # Customer TCR
                cust_tcr_text = gr.Text(
                    label="TCR",
                    value="",
                )

            with gr.Column(
                scale=2, 
                variant="compact",
            ):  
                gr.Markdown("### Customer Profiling")
                # Client profiling - 1 - customer persona + demographic + risk profile
                cust_profile_text = gr.Text(
                    label="Customer Demographic",
                    value="",
                    lines=5
                )
                gr.Markdown("### Finical News")
                # Related Finical News
                fin_news_text = gr.Text(
                    label="Financial News",
                    value="",
                    lines=3
                )
                gr.Markdown("### Talking Points")
                # Talking Points
                talking_points_text = gr.Text(
                    value="",
                    lines=3
                )

    cust_select.change(
        fn=update_customer_profile,
        inputs=[cust_select],
        outputs=[cust_seg_text, cust_invst_personal_txt, cust_tcr_text, cust_profile_text, fin_news_text, talking_points_text]
    )


RMAssistant.launch(
    height=1000
)