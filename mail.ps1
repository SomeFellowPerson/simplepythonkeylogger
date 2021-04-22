$Message = new-object Net.Mail.MailMessage
$smtp = new-object Net.Mail.SmtpClient("smtp.someserver.com", 587)
$smtp.Credentials = New-Object System.Net.NetworkCredential("test@gmail.com", "securepassword123");
$smtp.EnableSsl = $true
$smtp.Timeout = 400000
$Message.From = "test@gmail.com"
$Message.To.Add("test@gmail.com")
$Message.Attachments.Add("E:\somepath\somedirectory\logger.txt")
$smtp.Send($Message)