import quickstart
import gmail_api_bot

def remove_duplicates(arr):
        unique_arr = []
        for item in arr:
            if item not in unique_arr:
                unique_arr.append(item)
        return unique_arr

def remove_email_duplicates(array):
    unique_strings = set()

    # Iterate over the array
    for email in array:
        # Convert the email to lowercase
        lowercase_email = email.lower()

        # Check if the lowercase email is already in the set
        if lowercase_email not in unique_strings:
            # Add the lowercase email to the set
            unique_strings.add(lowercase_email)

    # Convert the set back to a list
    unique_array = list(unique_strings)

    return unique_array
def print_elements_start_with_number(arr):
    for element in arr:
        if element and element[0].isdigit():
            print(element)
            
quickstart.main()
email_list_array = quickstart.getEmailList()
provider_list = quickstart.getProviderList()


email_list = [email[0] for email in email_list_array]
email_count = len(email_list)

print(email_count)

# email_list = ['galieebailey@gmail.com', 'maxwellharris0303@outlook.com', 'dragongold0808@gmail.com']
# provider_list = ['BBXC', 'Hello ', 'sdfsdfwer']
# email_count = len(email_list)

# print(email_count)

index = 0
for _ in range(email_count):
    EMAIL_TITLE = "Revolutionize Your Medical Billing Process with Quality Healthcare Systems"
    EMAIL_BODY = f"""
    <html lang="en">
    <head> </head>
    <body>
        <div dir="ltr">
        Dear {provider_list[index]},<br /><br />I hope this email finds you well. I am
        writing to introduce you to Quality Healthcare Systems, a leading provider
        of comprehensive and efficient medical billing services tailored to meet
        the unique needs of healthcare providers like yourself.<br /><br />In
        today's dynamic healthcare landscape, the challenges of managing medical
        billing processes are more complex than ever. We understand the importance
        of streamlining revenue cycles, maximizing reimbursements, and ensuring
        compliance with ever-changing regulations. That's where Quality Healthcare
        Systems comes in.<br /><br />Here's how our medical billing services can
        benefit your practice:<br /><br />
        <ol>
            <li>
            <b>Efficiency and Accuracy:</b> Our cutting-edge technology and
            experienced billing professionals ensure accurate and efficient
            processing of claims, reducing errors and speeding up reimbursements.
            </li>
            <li>
            <b>Revenue Maximization: </b>We work tirelessly to optimize your
            revenue cycle, identifying and addressing potential revenue leakage
            points to maximize your financial returns.
            </li>
            <li>
            <b>Compliance Assurance:</b> Stay ahead of regulatory changes with our
            team of experts who are well-versed in the latest healthcare industry
            regulations, ensuring your practice remains compliant at all times.
            </li>
            <li>
            <b>Customized Solutions:</b> We understand that each healthcare
            practice is unique. Our services are tailored to meet the specific
            needs and challenges of your organization, ensuring a personalized
            approach to medical billing.
            </li>
            <li>
            <b>Transparency and Reporting: </b>Gain real-time insights into your
            financial performance through our transparent reporting systems. We
            provide you with the data you need to make informed decisions about
            your practice's financial health.
            </li>
        </ol>
        <br />We would be delighted to offer you a complimentary consultation to
        discuss how Quality Healthcare Systems can specifically address the needs
        of your practice. Our goal is to become a trusted partner in your success
        by improving your billing processes and boosting your bottom line.<br /><br />To
        schedule your free consultation or learn more about our services, please
        reply to this email or contact us at 855-QHS-5555.<br /><br />Thank you
        for considering Quality Healthcare Systems as your trusted medical billing
        partner. We look forward to the opportunity to support your practice's
        financial success.<br /><br />Best regards,
        </div>
    </body>
    </html>
    """
    service = gmail_api_bot.gmail_authenticate()
    aaa = gmail_api_bot.send_message(service, email_list[index], EMAIL_TITLE, EMAIL_BODY)
    print(aaa)

    index += 1

# alexandra.colideinstagram@gmail.com
# maxwellharris0303@outlook.com