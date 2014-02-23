########
# mailblast.py
# 
# _Author_ : Jhanani Dhakshnamoorthy (jhananidhakshnamoorthy2013@u.northwestern.edu)
# _Date_  : 11/1/2013
# _Description_ : This code is used for email delivery using smtp library in python
#
# Tested on OSX 10.8.5.
# Terminals running at least Python 2.5.2 to 3.3.2...
#
# To add email-IDs, include address in recipients (Line 33)
# To include cc mail recipients, add address in ccrecipients (Line 34)
#
# This file reads hastags from files Parent-hashtags-default-control-group.txt and healthcareprofessionals-default-control-group.txt
# 
# To send email newsletter, open terminal and type
# >>> python mailblast.py
# The newsletter will be emailed to the recipient.
########


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Sends email newslettter to multiple recipients and also includes cc recipients
def mailblast():
	gmail_user = 'babystepsnu@gmail.com'
	gmail_pwd = 'healthpoint'
	smtpserver = smtplib.SMTP("smtp.gmail.com",587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo
	smtpserver.login(gmail_user, gmail_pwd)

	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	recipients = ['jhananidhakshnamoorthy2013@u.northwestern.edu']
	ccrecipients = ['jhananidhakshnamoorthy2013@u.northwestern.edu']
	msg['Subject'] = 'Babysteps Weekly Report'
	msg['From'] = 'Babysteps'
	msg['To'] = ','.join(recipients)
	msg['Cc'] = ','.join(ccrecipients)
	html = getMessageContent()
	part2 = MIMEText(html, 'html')
	# Attach parts into message container.
	# According to RFC 2046, the last part of a multipart message, in this case
	# the HTML message, is best and preferred.
	msg.attach(part2)

	# Send the message via local SMTP server.
	smtpserver.sendmail(gmail_user, recipients+ccrecipients, msg.as_string())
	# sendmail function takes 3 arguments: sender's address, recipient's address
	# and message to send - here it is sent as one string.
	smtpserver.close()

 # Reads tags from output file
def getHashtagsContent(file):
	f = open(file)
	lines = f.readlines()
	l = lines
	lines = l[0].split(',')
	evenlines = [lines[i] for i in range(len(lines)) if i % 2 == 0]
	evenlines = [e[2:] for e in evenlines]
	ht = [e.strip('u') for e in evenlines]
	ht2 = [e.strip('\'') for e in ht]
	f.close()
	htmlc = ""
	tr = "<tr>"
	rend = "</tr>"
	td = "</td>"
	evenrow = """<td align = "left" style="font-size:14px;font-family:Arial;font-weight:400;font-style:normal;border-top-color:#D3D3D3;border-top: 1px solid #D3D3D3;border-bottom-color:#D3D3D3;border-bottom: 1px solid #D3D3D3;border-left-color:#D3D3D3;border-left: 1px solid #D3D3D3;border-right-color:#D3D3D3;
               border-right: 1px solid #D3D3D3 " width="363" height="24" bgcolor="#D5EFF5">"""
	oddrow = """<td align = "left" style="font-size:14px;font-family:Arial;font-weight:400;font-style:normal;border-top-color:#D3D3D3;border-top: 1px solid #D3D3D3;border-bottom-color:#D3D3D3;border-bottom: 1px solid #D3D3D3;border-left-color:#D3D3D3;border-left: 1px solid #D3D3D3;border-right-color:#D3D3D3;
             border-right: 1px solid #D3D3D3 " width="363" height="24" bgcolor="#FAFAFA">""" 
	linect = 0    
	for i in range(0, 20, 2):
		if(linect%2 == 0):
			htmlc+= tr+evenrow+ht2[i]+td+evenrow+ht2[i+1]+td+rend
		else:
			htmlc+= tr+oddrow+ht2[i]+td+oddrow+ht2[i+1]+td+rend
		linect += 1

	return htmlc

                                                                      

# Creates html content for newsletter, embeds hashtags and posts in online forums
def getMessageContent():
	html = """\
	<html>
	        <head>
	                <meta content="text/html; charset=UTF-8" http-equiv="Content-Type" />
	<!-- Facebook sharing information tags -->              <meta content="*|MC:SUBJECT|*" property="og:title" />
	                <title>*|MC:SUBJECT|*</title>
	                <style type="text/css">
	/* Client-specific Styles */
	                        #outlook a{padding:0;} /* Force Outlook to provide a "view in browser" button. */
	                        body{width:100% !important;} .ReadMsgBody{width:100%;} .ExternalClass{width:100%;} /* Force Hotmail to display emails at full width */
	                        body{-webkit-text-size-adjust:none;} /* Prevent Webkit platforms from changing default text sizes. */
	                        
	                        /* Reset Styles */
	                        body{margin:0; padding:0;}
	                        img{border:0; height:auto; line-height:100%; outline:none; text-decoration:none;}
	                        table td{border-collapse:collapse;}
	                        #backgroundTable{height:100% !important; margin:0; padding:0; width:100% !important;}
	                        
	                        /* Template Styles */
	                        
	                        /* /\/\/\/\/\/\/\/\/\/\ STANDARD STYLING: COMMON PAGE ELEMENTS /\/\/\/\/\/\/\/\/\/\ */
	                        
	                        /**
	                        * @tab Page
	                        * @section background color
	                        * @tip Set the background color for your email. You may want to choose one that matches your company's branding.
	                        * @theme page
	                        */
	                        body, #backgroundTable{
	                                /*@editable*/ background-color:#FAFAFA;
	                        }
	                        
	                        /**
	                        * @tab Page
	                        * @section email border
	                        * @tip Set the border for your email.
	                        */
	                        #templateContainer{
	                                /*@editable*/ border: 1px solid #DDDDDD;
	                        }
	                        
	                        /**
	                        * @tab Page
	                        * @section heading 1
	                        * @tip Set the styling for all first-level headings in your emails. These should be the largest of your headings.
	                        * @style heading 1
	                        */
	                        h1, .h1{
	                                /*@editable*/ color:#202020;
	                                display:block;
	                                /*@editable*/ font-family:Arial;
	                                /*@editable*/ font-size:34px;
	                                /*@editable*/ font-weight:bold;
	                                /*@editable*/ line-height:100%;
	                                margin-top:0;
	                                margin-right:0;
	                                margin-bottom:10px;
	                                margin-left:0;
	                                /*@editable*/ text-align:left;
	                        }

	                        /**
	                        * @tab Page
	                        * @section heading 2
	                        * @tip Set the styling for all second-level headings in your emails.
	                        * @style heading 2
	                        */
	                        h2, .h2{
	                                /*@editable*/ color:#202020;
	                                display:block;
	                                /*@editable*/ font-family:Arial;
	                                /*@editable*/ font-size:30px;
	                                /*@editable*/ font-weight:bold;
	                                /*@editable*/ line-height:100%;
	                                margin-top:0;
	                                margin-right:0;
	                                margin-bottom:10px;
	                                margin-left:0;
	                                /*@editable*/ text-align:left;
	                        }

	                        /**
	                        * @tab Page
	                        * @section heading 3
	                        * @tip Set the styling for all third-level headings in your emails.
	                        * @style heading 3
	                        */
	                        h3, .h3{
	                                /*@editable*/ color:#202020;
	                                display:block;
	                                /*@editable*/ font-family:Arial;
	                                /*@editable*/ font-size:26px;
	                                /*@editable*/ font-weight:bold;
	                                /*@editable*/ line-height:100%;
	                                margin-top:0;
	                                margin-right:0;
	                                margin-bottom:10px;
	                                margin-left:0;
	                                /*@editable*/ text-align:left;
	                        }

	                        /**
	                        * @tab Page
	                        * @section heading 4
	                        * @tip Set the styling for all fourth-level headings in your emails. These should be the smallest of your headings.
	                        * @style heading 4
	                        */
	                        h4, .h4{
	                                /*@editable*/ color:#202020;
	                                display:block;
	                                /*@editable*/ font-family:Arial;
	                                /*@editable*/ font-size:22px;
	                                /*@editable*/ font-weight:bold;
	                                /*@editable*/ line-height:100%;
	                                margin-top:0;
	                                margin-right:0;
	                                margin-bottom:10px;
	                                margin-left:0;
	                                /*@editable*/ text-align:left;
	                        }
	                        
	                        /* /\/\/\/\/\/\/\/\/\/\ STANDARD STYLING: PREHEADER /\/\/\/\/\/\/\/\/\/\ */
	                        
	                        /**
	                        * @tab Header
	                        * @section preheader style
	                        * @tip Set the background color for your email's preheader area.
	                        * @theme page
	                        */
	                        #templatePreheader{
	                                /*@editable*/ background-color:#FAFAFA;
	                        }
	                        
	                        /**
	                        * @tab Header
	                        * @section preheader text
	                        * @tip Set the styling for your email's preheader text. Choose a size and color that is easy to read.
	                        */
	                        .preheaderContent div{
	                                /*@editable*/ color:#505050;
	                                /*@editable*/ font-family:Arial;
	                                /*@editable*/ font-size:10px;
	                                /*@editable*/ line-height:100%;
	                                /*@editable*/ text-align:left;
	                        }
	                        
	                        /**
	                        * @tab Header
	                        * @section preheader link
	                        * @tip Set the styling for your email's preheader links. Choose a color that helps them stand out from your text.
	                        */
	                        .preheaderContent div a:link, .preheaderContent div a:visited, /* Yahoo! Mail Override */ .preheaderContent div a .yshortcuts /* Yahoo! Mail Override */{
	                                /*@editable*/ color:#336699;
	                                /*@editable*/ font-weight:normal;
	                                /*@editable*/ text-decoration:underline;
	                        }
	                        

	                        
	                        /* /\/\/\/\/\/\/\/\/\/\ STANDARD STYLING: HEADER /\/\/\/\/\/\/\/\/\/\ */
	                        
	                        /**
	                        * @tab Header
	                        * @section header style
	                        * @tip Set the background color and border for your email's header area.
	                        * @theme header
	                        */
	                        #templateHeader{
	                                /*@editable*/ background-color:#FFFFFF;
	                                /*@editable*/ border-bottom:0;
	                        }
	                        
	                        /**
	                        * @tab Header
	                        * @section header text
	                        * @tip Set the styling for your email's header text. Choose a size and color that is easy to read.
	                        */
	                        .headerContent{
	                                /*@editable*/ color:#202020;
	                                /*@editable*/ font-family:Arial;
	                                /*@editable*/ font-size:34px;
	                                /*@editable*/ font-weight:bold;
	                                /*@editable*/ line-height:100%;
	                                /*@editable*/ padding:0;
	                                /*@editable*/ text-align:center;
	                                /*@editable*/ vertical-align:middle;
	                        }
	                        
	                        /**
	                        * @tab Header
	                        * @section header link
	                        * @tip Set the styling for your email's header links. Choose a color that helps them stand out from your text.
	                        */
	                        .headerContent a:link, .headerContent a:visited, /* Yahoo! Mail Override */ .headerContent a .yshortcuts /* Yahoo! Mail Override */{
	                                /*@editable*/ color:#336699;
	                                /*@editable*/ font-weight:normal;
	                                /*@editable*/ text-decoration:underline;
	                        }
	                        
	                        #headerImage{
	                                height:auto;
	                                max-width:600px;
	                        }
	                        
	                        /* /\/\/\/\/\/\/\/\/\/\ STANDARD STYLING: MAIN BODY /\/\/\/\/\/\/\/\/\/\ */

	                        /**
	                        * @tab Body
	                        * @section body style
	                        * @tip Set the background color for your email's body area.
	                        */
	                        #templateContainer, .bodyContent{
	                                /*@editable*/ background-color:#FFFFFF;
	                        }
	                        
	                        /**
	                        * @tab Body
	                        * @section body text
	                        * @tip Set the styling for your email's main content text. Choose a size and color that is easy to read.
	                        * @theme main
	                        */
	                        .bodyContent div{
	                                /*@editable*/ color:#505050;
	                                /*@editable*/ font-family:Arial;
	                                /*@editable*/ font-size:14px;
	                                /*@editable*/ line-height:150%;
	                                /*@editable*/ text-align:left;
	                        }
	                        
	                        /**
	                        * @tab Body
	                        * @section body link
	                        * @tip Set the styling for your email's main content links. Choose a color that helps them stand out from your text.
	                        */
	                        .bodyContent div a:link, .bodyContent div a:visited, /* Yahoo! Mail Override */ .bodyContent div a .yshortcuts /* Yahoo! Mail Override */{
	                                /*@editable*/ color:#336699;
	                                /*@editable*/ font-weight:normal;
	                                /*@editable*/ text-decoration:underline;
	                        }
	                        
	                        .bodyContent img{
	                                display:inline;
	                                height:auto;
	                        }
	                        
	                        /* /\/\/\/\/\/\/\/\/\/\ STANDARD STYLING: FOOTER /\/\/\/\/\/\/\/\/\/\ */
	                        
	                        /**
	                        * @tab Footer
	                        * @section footer style
	                        * @tip Set the background color and top border for your email's footer area.
	                        * @theme footer
	                        */
	                        #templateFooter{
	                                /*@editable*/ background-color:#FFFFFF;
	                                /*@editable*/ border-top:0;
	                        }
	                        
	                        /**
	                        * @tab Footer
	                        * @section footer text
	                        * @tip Set the styling for your email's footer text. Choose a size and color that is easy to read.
	                        * @theme footer
	                        */
	                        .footerContent div{
	                                /*@editable*/ color:#707070;
	                                /*@editable*/ font-family:Arial;
	                                /*@editable*/ font-size:12px;
	                                /*@editable*/ line-height:125%;
	                                /*@editable*/ text-align:left;
	                        }
	                        
	                        /**
	                        * @tab Footer
	                        * @section footer link
	                        * @tip Set the styling for your email's footer links. Choose a color that helps them stand out from your text.
	                        */
	                        .footerContent div a:link, .footerContent div a:visited, /* Yahoo! Mail Override */ .footerContent div a .yshortcuts /* Yahoo! Mail Override */{
	                                /*@editable*/ color:#336699;
	                                /*@editable*/ font-weight:normal;
	                                /*@editable*/ text-decoration:underline;
	                        }
	                        
	                        .footerContent img{
	                                display:inline;
	                        }
	                        
	                        /**
	                        * @tab Footer
	                        * @section social bar style
	                        * @tip Set the background color and border for your email's footer social bar.
	                        * @theme footer
	                        */
	                        #social{
	                                /*@editable*/ background-color:#FAFAFA;
	                                /*@editable*/ border:0;
	                        }
	                        
	                        /**
	                        * @tab Footer
	                        * @section social bar style
	                        * @tip Set the background color and border for your email's footer social bar.
	                        */
	                        #social div{
	                                /*@editable*/ text-align:center;
	                        }
	                        
	                        /**
	                        * @tab Footer
	                        * @section utility bar style
	                        * @tip Set the background color and border for your email's footer utility bar.
	                        * @theme footer
	                        */
	                        #utility{
	                                /*@editable*/ background-color:#FFFFFF;
	                                /*@editable*/ border:0;
	                        }

	                        /**
	                        * @tab Footer
	                        * @section utility bar style
	                        * @tip Set the background color and border for your email's footer utility bar.
	                        */
	                        #utility div{
	                                /*@editable*/ text-align:center;
	                        }
	                        
	                        #monkeyRewards img{
	                                max-width:190px;
	                        }               </style>
	        </head>
	        <body leftmargin="0" marginheight="0" marginwidth="0" offset="0" topmargin="0">
	                <center>
	                        <table border="0" cellpadding="0" cellspacing="0" id="templateContainer" style="border-collapse: collapse; border: 0px; background-color: rgb(242, 242, 242);" width="600">
	                                <tbody>
	                                        <tr>
	                                                <td align="center" valign="top">
	                                                        <table border="0" cellpadding="0" cellspacing="0" id="templatePreheader" style="border-collapse: collapse; background-color: rgb(255, 255, 255); border-top-width: 0px; border-bottom-width: 0px;" width="600">
	                                                                <tbody>
	                                                                        <tr>
	                                                                                <td class="preheaderContainer tpl-container dojoDndSource dojoDndTarget dojoDndContainer" mc:container="preheader_container" mccontainer="preheader_container" style="padding-top: 9px;" valign="top">
	                                                                                        <div class="mojoMcBlock tpl-block dojoDndItem" id="mojo_neapolitan_preview_McBlock_0" style="position: relative;" widgetid="mojo_neapolitan_preview_McBlock_0">
	                                                                                                <div data-dojo-attach-point="containerNode">
	                                                                                                        <table border="0" cellpadding="0" cellspacing="0" class="mcnTextBlock" style="border-collapse: collapse;" width="100%">
	                                                                                                                <tbody class="mcnTextBlockOuter">
	                                                                                                                        <tr>
	                                                                                                                                <td class="mcnTextBlockInner" valign="top">
	                                                                                                                                        <table align="left" border="0" cellpadding="0" cellspacing="0" class="mcnTextContentContainer" style="border-collapse: collapse;" width="366">
	                                                                                                                                                <tbody>
	                                                                                                                                                        <tr>
	                                                                                                                                                                <td class="mcnTextContent" style="color: rgb(96, 96, 96); font-family: Helvetica; font-size: 13px; line-height: 16px; padding: 9px 0px 9px 18px;" valign="top">
	                                                                                                                                                                        Your weekly report of social media activity from parents and child specialists brought to you by Babysteps</td>
	                                                                                                                                                        </tr>
	                                                                                                                                                </tbody>
	                                                                                                                                        </table>
	                                                                                                                                </td>
	                                                                                                                        </tr>
	                                                                                                                </tbody>
	                                                                                                        </table>
	                                                                                                </div>
	                                                                                        </div>
	                                                                                </td>
	                                                                        </tr>
	                                                                </tbody>
	                                                        </table>
	                                                </td>
	                                        </tr>
	                                        <tr>
	                                                <td align="center" valign="top">
	                                                        <table border="0" cellpadding="0" cellspacing="0" id="templateHeader" style="border-collapse: collapse; border-top-width: 0px;" width="600">
	                                                                <tbody>
	                                                                        <tr>
	                                                                                <td class="headerContainer tpl-container dojoDndSource dojoDndTarget dojoDndContainer" mc:container="header_container" mccontainer="header_container" valign="top">
	                                                                                        <div class="mojoMcBlock tpl-block dojoDndItem" id="mojo_neapolitan_preview_McBlock_1" style="position: relative;" widgetid="mojo_neapolitan_preview_McBlock_1">
	                                                                                                <div data-dojo-attach-point="containerNode">
	                                                                                                        <table border="0" cellpadding="0" cellspacing="0" class="mcnImageBlock" style="border-collapse: collapse;" width="100%">
	                                                                                                                <tbody class="mcnImageBlockOuter">
	                                                                                                                        <tr>
	                                                                                                                                <td class="mcnImageBlockInner" style="padding: 9px;" valign="top">
	                                                                                                                                        <table align="left" border="0" cellpadding="0" cellspacing="0" class="mcnImageContentContainer" style="border-collapse: collapse;" width="100%">
	                                                                                                                                                <tbody>
	                                                                                                                                                        <tr>
	                                                                                                                                                                <td class="mcnImageContent" style="padding: 0px 9px;" valign="top">
	                                                                                                                                                                        <img align="left" alt="" class="mcnImage blockDropTarget" id="mojo_neapolitan_preview_ImageUploader_0" src="https://gallery.mailchimp.com/6b764148e76cb9be1e32702bc/images/babystepslogo.jpg" style="vertical-align: bottom; max-width: 550px; padding-bottom: 0px; display: inline !important;" widgetid="mojo_neapolitan_preview_ImageUploader_0" width="600" /></td>
	                                                                                                                                                        </tr>
	                                                                                                                                                </tbody>
	                                                                                                                                        </table>
	                                                                                                                                </td>
	                                                                                                                        </tr>
	                                                                                                                </tbody>
	                                                                                                        </table>
	                                                                                                </div>
	                                                                                        </div>
	                                                                                </td>
	                                                                        </tr>
	                                                                </tbody>
	                                                        </table>
	                                                </td>
	                                        </tr>
	                                        <tr>
	                                                <td align="center" valign="top">
	                                                        <table border="0" cellpadding="0" cellspacing="0" id="templateBody" style="border-collapse: collapse; background-color: rgb(255, 255, 255); border-top-width: 0px; border-bottom-width: 0px;" width="600">
	                                                                <tbody>
	                                                                        <tr>
	                                                                                <td class="bodyContainer tpl-container dojoDndSource dojoDndTarget dojoDndContainer" mc:container="body_container" mccontainer="body_container" valign="top">
	                                                                                        <div class="mojoMcBlock tpl-block dojoDndItem" id="mojo_neapolitan_preview_McBlock_2" style="position: relative;" widgetid="mojo_neapolitan_preview_McBlock_2">
	                                                                                                <div data-dojo-attach-point="containerNode">
	                                                                                                        <table border="0" cellpadding="0" cellspacing="0" class="mcnTextBlock" style="border-collapse: collapse;" width="100%">
	                                                                                                                <tbody class="mcnTextBlockOuter">
	                                                                                                                        <tr>
	                                                                                                                                <td class="mcnTextBlockInner" valign="top">
	                                                                                                                                        <table align="left" border="0" cellpadding="0" cellspacing="0" class="mcnTextContentContainer" style="border-collapse: collapse;" width="600">
	                                                                                                                                                <tbody>
	                                                                                                                                                        <tr>
	                                                                                                                                                                <td class="mcnTextContent" style="color: rgb(96, 96, 96); font-family: Helvetica; font-size: 13px; line-height: 19px; padding: 9px 18px;" valign="top">
	                                                                                                                                                                        <h1 style="margin-bottom: 0px; padding: 0px; font-family: Helvetica; font-size: 40px; line-height: 50px; letter-spacing: -1px; color: rgb(96, 96, 96) !important;">
	                                                                                                                                                                                Dear Pathways Team&nbsp;</h1>
	                                                                                                                                                                        
	                                                                                                                                                                        <h3 style="margin-bottom: 0px; padding: 0px; font-family: Helvetica; font-size: 18px; line-height: 22px; letter-spacing: -0.5px; color: rgb(96, 96, 96) !important;">
	                                                                                                                                                                                Here are the recent hashtags you might find useful</h3> """
	
	htmlp = """                                                                                                                                                                        
	<p style="margin: 1em 0px; font-size: 15px; line-height: 22px;"><a class="link" style="word-wrap: break-word; color: rgb(109, 198, 221);">Here are the hashtags parents used on Twitter in the past week.</a></p>
	 	 <div align="center"><table id="plugandtable" width="550" height="120" cellpadding="5" border="1" cellspacing="0" style="border-color:#000000;font-size:11px; border-collapse:collapse"> """+getHashtagsContent("Parent-hashtags-default-control-group.txt")+"</table></div>"	  

	htmlhcp ="""
	<p style="margin: 1em 0px; font-size: 15px; line-height: 22px;"><a class="link" style="word-wrap: break-word; color: rgb(109, 198, 221);">Here are the hashtags HealthCare Professionals used on Twitter in the past week.</a></p>
	 	 <div align="center"><table id="plugandtable" width="550" height="120" cellpadding="5" border="1" cellspacing="0" style="border-color:#000000;font-size:11px; border-collapse:collapse"> """+getHashtagsContent("healthcareprofessional-hashtags-default-control-group.txt")+"</table></div></td></tr></tbody></table></td></tr></tbody></table></div></div>"
                                                                          

	html4 ="""
	<div class="mojoMcBlock tpl-block dojoDndItem" id="mojo_neapolitan_preview_McBlock_3" style="position: relative;" widgetid="mojo_neapolitan_preview_McBlock_3">
	    <div data-dojo-attach-point="containerNode">
	        <table border="0" cellpadding="0" cellspacing="0" class="mcnTextBlock" style="border-collapse: collapse;" width="100%">
	            <tbody class="mcnTextBlockOuter">
	                <tr>
	                    <td class="mcnTextBlockInner" valign="top">
	                        <table align="left" border="0" cellpadding="0" cellspacing="0" class="mcnTextContentContainer" style="border-collapse: collapse;" width="600">
	                                <tbody>
	                                	<tr>
	                                        <td class="mcnTextContent" style="color: rgb(96, 96, 96); font-family: Helvetica; font-size: 13px; line-height: 19px; padding: 9px 18px;" valign="top">
	                                            <h3 class="mc-toc-title" style="margin-bottom: 0px; padding: 0px; font-family: Helvetica; font-size: 18px; line-height: 22px; letter-spacing: -0.5px; color: rgb(96, 96, 96) !important;">
	                                            Here are some recent forum discussions you might want to reply to</h3>
	                                            	<h2 class="mc-toc-title" style="margin-bottom: 0px; padding: 0px; font-family: Helvetica; font-size: 14px; line-height: 22px; letter-spacing: -0.5px; color: rgb(96, 96, 96) !important;">
	                                            	Recent threads about Torticollis &nbsp;</h2>
	                                                	<p style="margin: 1em 0px; font-size: 15px; line-height: 22px;">
	                                    					<a class="mc-template-link" href="http://community.babycenter.com/post/a36965266/any_progress" style="word-wrap: break-word; color: rgb(109, 198, 221);" target="_blank">Any Progress&nbsp;</a></p>
	                                    						<p style="margin: 1em 0px; font-size: 15px; line-height: 22px;">
	                                    							<a class="mc-template-link" href="http://community.babycenter.com/post/a31060539/new_to_board._stressed_out" style="word-wrap: break-word; color: rgb(109, 198, 221);" target="_blank">New to board. Stressed Out&nbsp;</a></p>
	                                    							<p style="margin: 1em 0px; font-size: 15px; line-height: 22px;">
	                                    								<a class="mc-template-link" href="http://community.babycenter.com/post/a27661337/13_month_old_with_persistant_tilt" style="word-wrap: break-word; color: rgb(109, 198, 221);" target="_blank">13 Month Old With Persistant Tilt&nbsp;</a></p>
	                                    									<p style="margin: 1em 0px; font-size: 15px; line-height: 22px;">
	                                    										<a class="mc-template-link" href="http://community.babycenter.com/post/a30861853/flat_head...see_photo" style="word-wrap: break-word; color: rgb(109, 198, 221);" target="_blank">Flat Head See Photo&nbsp;</a></p>
	                                    											<p style="margin: 1em 0px; font-size: 15px; line-height: 22px;">
	                                    												<a class="mc-template-link" href="http://community.babycenter.com/post/a40380976/question_for_those_who_completed_pt" style="word-wrap: break-word; color: rgb(109, 198, 221);" target="_blank">Question For Those Who Completed Pt&nbsp;</a></p>
	                                    													<h2 class="mc-toc-title" style="margin-bottom: 0px; padding: 0px; font-family: Helvetica; font-size: 14px; line-height: 22px; letter-spacing: -0.5px; color: rgb(96, 96, 96) !important;">
	                                            												Recent thread about Plagiocephaly &nbsp;</h2>
	                                                												<p style="margin: 1em 0px; font-size: 15px; line-height: 22px;">
	                                    																<a class="mc-template-link" href="http://community.babycenter.com/post/a46005364/plagiocephaly_22_months" style="word-wrap: break-word; color: rgb(109, 198, 221);" target="_blank">Plagiocephaly 22 Months&nbsp;</a></p>
	                                    																	<p style="margin: 1em 0px; font-size: 15px; line-height: 22px;">
	                                    																		<a class="mc-template-link" href="http://community.babycenter.com/post/a44572657/anyones_baby_have_tight_muscle_under_arm_on_body_as_well_as_neck" style="word-wrap: break-word; color: rgb(109, 198, 221);" target="_blank">Anyones Baby Have Tight Muscle Under Arm On Body As Well Ns Neck&nbsp;</a></p>
	                                                                                                                                      						</td>
	                                                                                                                                                        </tr>
	                                                                                                                                                </tbody>
	                                                                                                                                        </table>
	                                                                                                                                </td>
	                                                                                                                        </tr>
	                                                                                                                </tbody>
	                                                                                                        </table>
	                                                                                                </div>                  
	                                                                                        </div>
	                                                                                        
	                                                                                        <div class="mojoMcBlock tpl-block dojoDndItem" id="mojo_neapolitan_preview_McBlock_4" style="position: relative;" widgetid="mojo_neapolitan_preview_McBlock_4">
	                                                                                                <div data-dojo-attach-point="containerNode">
	                                                                                                        <table border="0" cellpadding="0" cellspacing="0" class="mcnTextBlock" style="border-collapse: collapse;" width="100%">
	                                                                                                                <tbody class="mcnTextBlockOuter">
	                                                                                                                        <tr>
	                                                                                                                                <td class="mcnTextBlockInner" valign="top">
	                                                                                                                                        <table align="left" border="0" cellpadding="0" cellspacing="0" class="mcnTextContentContainer" style="border-collapse: collapse;" width="600">
	                                                                                                                                                <tbody>
	                                                                                                                                                        <tr>
	                                                                                                                                                                <td class="mcnTextContent" style="color: rgb(96, 96, 96); font-family: Helvetica; font-size: 13px; line-height: 19px; padding: 9px 18px;" valign="top">
	                                                                                                                                                                        &nbsp;</td>
	                                                                                                                                                        </tr>
	                                                                                                                                                </tbody>
	                                                                                                                                        </table>
	                                                                                                                                </td>
	                                                                                                                        </tr>
	                                                                                                                </tbody>
	                                                                                                        </table>
	                                                                                                </div>
	                                                                                        </div>
	                                                                                </td>
	                                                                        </tr>
	                                                                </tbody>
	                                                        </table>
	                                                </td>
	                                        </tr>
	                                        <tr>
	                                                <td align="center" valign="top">
	                                                        <table border="0" cellpadding="0" cellspacing="0" id="templateFooter" style="border-collapse: collapse; border-bottom-width: 0px;" width="600">
	                                                                <tbody>
	                                                                        <tr>
	                                                                                <td class="footerContainer tpl-container dojoDndSource dojoDndTarget dojoDndContainer" mc:container="footer_container" mccontainer="footer_container" style="padding-bottom: 9px;" valign="top">
	                                                                                        <div class="mojoMcBlock tpl-block dojoDndItem" id="mojo_neapolitan_preview_McBlock_5" style="position: relative;" widgetid="mojo_neapolitan_preview_McBlock_5">
	                                                                                                <div data-dojo-attach-point="containerNode">
	                                                                                                        <table border="0" cellpadding="0" cellspacing="0" class="mcnTextBlock" style="border-collapse: collapse;" width="100%">
	                                                                                                                <tbody class="mcnTextBlockOuter">
	                                                                                                                        <tr>
	                                                                                                                                <td class="mcnTextBlockInner" valign="top">
	                                                                                                                                        <table align="left" border="0" cellpadding="0" cellspacing="0" class="mcnTextContentContainer" style="border-collapse: collapse;" width="600">
	                                                                                                                                                <tbody>
	                                                                                                                                                        <tr>
	                                                                                                                                                                <td class="mcnTextContent" style="color: rgb(96, 96, 96); font-family: Helvetica; font-size: 11px; line-height: 13px; padding: 9px 18px;" valign="top">
	                                                                                                                                                                        <em>Copyright &copy; *babysteps* , All rights reserved.</em><br />
	                                                                                                                                                                        <br />
	                                                                                                                                                                        <br />
	                                                                                                                                                                        <strong>Our mailing address is:</strong><br />
	                                                                                                                                                                        <em>babystepsnu@gmail.com</em><br />
	                                                                                                                                                                        <br />
	                                                                                                                                                                        </td>
	                                                                                                                                                        </tr>
	                                                                                                                                                </tbody>
	                                                                                                                                        </table>
	                                                                                                                                </td>
	                                                                                                                        </tr>
	                                                                                                                </tbody>
	                                                                                                        </table>
	                                                                                                </div>
	                                                                                        </div>
	                                                                                </td>
	                                                                        </tr>
	                                                                </tbody>
	                                                        </table>
	                                                </td>
	                                        </tr>
	                                </tbody>
	                        </table>
	                </center></body>
	</html>
	"""
	return html+htmlp+htmlhcp+html4

mailblast()



