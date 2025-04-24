# from dotenv import load_dotenv
# from flask import Flask, render_template, request, jsonify
# from ice_breaker import ice_break_with
#
# load_dotenv()
#
# app=Flask(__name__)
#
# @app.route("/")
# def index():
#     return render_template("index.html")
#
# @app.route("/process", methods=["POST"])
# def process():
#     name = request.form["name"]
#     summary, profile_pic_url = ice_break_with(name=name)
#     return jsonify(
#         {
#             "summary_and_facts": summary.to_dict(),
#             "photoUrl": profile_pic_url,
#         }
#     )
# if __name__=="__main__":
#     app.run(host="0.0.0.0", port=5001, debug=True)
#
#

import streamlit as st
from dotenv import load_dotenv
from ice_breaker import ice_break_with


def main():
    load_dotenv()

    st.title("Ice Breaker")

    # Input field for name
    name = st.text_input("Enter Name:")

    # Button to trigger the process
    if st.button("Do Your Magic"):
        if name:
            # Show a spinner while processing
            with st.spinner("Processing..."):
                # Get information from ice_break_with function
                summary, profile_pic_url = ice_break_with(name=name)

                # Display results
                if profile_pic_url:
                    st.image(profile_pic_url, width=300)

                # Display summary
                st.header("Summary")
                st.write(summary.summary)

                # Display interesting facts
                st.header("Interesting Facts")
                for fact in summary.facts:
                    st.markdown(f"- {fact}")

                # If you add ice breakers and topics of interest in the future
                # Uncomment these sections:

                # # Display ice breakers if available
                # if hasattr(summary, 'ice_breakers'):
                #     st.header("Ice Breakers")
                #     for ice_breaker in summary.ice_breakers:
                #         st.markdown(f"- {ice_breaker}")

                # # Display topics of interest if available
                # if hasattr(summary, 'topics_of_interest'):
                #     st.header("Topics of Interest")
                #     for topic in summary.topics_of_interest:
                #         st.markdown(f"- {topic}")
        else:
            st.warning("Please enter a name to continue.")


if __name__ == "__main__":
    main()
