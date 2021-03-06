# Zai Clock in Software

Welcome, this project is 
this project is a clock in software for small business

This project is a MVP. In future versions will be changed in a SAAS model app and will be integrated with full payroll, automatic HMRC submissions, mobile apps and many more.

See this project on live enviroment on GitHub Pages here: <https://zai-clock-in-software.herokuapp.com/>

![Website on different screen sizes](readme-assets/img/screens.png)



### User Stories

As a employer:

- I want users to be able to easily navigate my website on any device.
- I want to bo able to add, edit employees.
- I want to be able to check presence.
- I want my website to be accessible to anyone even for screen readers.
- I want to be able to personalize my software

As a employee:

- I want to be able to clock in and out easy and fast.
- I want to know if my action was successfully.

## Features

<details>
<summary>Click To Expand Features</summary>

### Navigation

- Same navigation menu is used across all pages for consistency, but is hidden from user that is not authenticated because in index page is no need for navbar.


![NavBar Desktop](readme-assets/img/navbar-desktop.png)

- Navigation was designed to be easy to use and to understand.

![NavBar Mobile](readme-assets/img/navbar-mobile.png)

- Navigation was designed to work well on all devices.


### Index Screen

Index Screen was designed with employee in mind. Only required features are in this page. NFC is working only in Google Chrome For Android, and is activated if is possible.

- Index Screen Desktop

![Index Screen Desktop](readme-assets/img/index-desktop.png)

- Index Screen Tablet ( NFC INACTIVE )

![Index Screen Tablet](readme-assets/img/index-tablet.png)

- Index Screen Mobile ( NFC ACTIVE )
- NFC READY message appear on screen only if device is compatible, NFC is active and permissions given

![Index Screen Mobile](readme-assets/img/index-mobile.jpg)

### Registration Page

- Registration page is designed with employee, hr employees in mind
![Registration Page Desktop](readme-assets/img/registration-desktop.png)

- Registration Page Mobile

![Registration Page Mobile](readme-assets/img/registration-mobile.png)

### Verification Email

Once registration was successful email verification is required.

- Verification Email Desktop

![Verification Email Desktop](readme-assets/img/verification-email-desktop.png)

- Verification Email Mobile Top Part

![Verification Email Mobile Top Part](readme-assets/img/verification-mobile-top.jpg)

- Verification Email Mobile Bottom Part

![Verification Email Mobile Bottom Part](readme-assets/img/verification-mobile-bottom.jpg)

### Verify Page

Once user click the email is redirected to verification page where have to input email address and secret code from email.

- Verification Page Desktop

![Verification Page Desktop](readme-assets/img/verify-desktop.png)

- Verification Page Mobile

![Verification Page Mobile](readme-assets/img/verify-mobile.png)


### Resend Verification

If user don't have verification code, can request to be resent to email address.

- Resend Verification Page Desktop

![Resend Verification Page Desktop](readme-assets/img/resend-verification-page-desktop.png)

- Resend Verification Page Mobile

![Resend Verification Page Mobile](readme-assets/img/resend-verification-page-mobile.png)


### Login Page

Once email is verified user is redirected to login. 

- Login Page Desktop

![Login Page Desktop](readme-assets/img/login-page-desktop.png)

- Login Page Mobile

![Login Page Mobile](readme-assets/img/login-page-mobile.png)


### Dashboard Page

Once email is verified user is redirected to login. 

- Dashboard Desktop

![Dashboard Desktop](readme-assets/img/dashboard-desktop.png)

- Dashboard Mobile

![Dashboard Mobile](readme-assets/img/dashboard-mobile.png)

### Settings Page

Settings page give the power to end user to customise the lock of his brand now software by changing brand name, navbar-footer color and text color and google font. More settings will be added latter. 

- Settings Page Desktop

![Settings Page Desktop](readme-assets/img/settings-page-desktop.png)

- Settings Page Mobile

![Settings Page Mobile](readme-assets/img/settings-page-mobile.png)

### Employer Profile Page( HR -Department)

In this page employer or hr department can see or update their details

- Employer Profile Page Desktop

![Employer Profile Page Desktop](readme-assets/img/profile-page-desktop.png)

- Employer Profile Page Mobile

![Employer Profile Page Mobile](readme-assets/img/profile-page-mobile.png)


### Working Now Page

In this page we can check who is working now, and clock in times.

- Working Now Page Desktop

![Working Now Page Desktop](readme-assets/img/working-now-desktop.png)

- Working Now Page Mobile

![Working Now Page Mobile](readme-assets/img/working-now-mobile.png)


### Home Now Page

In this page we can check who is not working now, and clock-out times.

- Home Now Page Desktop

![Home Now Page Desktop](readme-assets/img/home-now-desktop.png)

- Home Now Page Mobile

![Home Now Page Mobile](readme-assets/img/home-now-mobile.png)


### Add Employee Page

In this page we can add an employee. Clock nr is unique and because of that we generate this number automatically.

- Add Employee Page Desktop

![Add Employee Page Desktop](readme-assets/img/add-employee-desktop.png)

- Add Employee Page Mobile

![Add Employee Page Mobile](readme-assets/img/add-employee-mobile.png)


### Employees Page

In this page we can see all employees. And we have an link to edit page if is required.

- Employees Page Desktop

![Employees Page Desktop](readme-assets/img/employees-page-desktop.png)

- Employees Page Mobile

![Employees Page Mobile](readme-assets/img/employees-page-mobile.png)


### Edit Employees Page

In this page we can edit employee details, excepting Clock Nr.

- Edit Employees Page Desktop

![Edit Employees Page Desktop](readme-assets/img/edit-employee-desktop.png)

- Edit Employees Page Mobile

![Edit Employees Page Mobile](readme-assets/img/edit-employee-mobile.png)


### Delete Employees PopUp

In this page we can delete employee details, action is irreversible. We use clock in like a security.


- Delete Employees PopUp

![Delete Employees PopUp Desktop](readme-assets/img/delete-employee-desktop.png)

- Delete Employees PopUp Mobile

![Delete Employees PopUp Mobile](readme-assets/img/delete-employee-mobile.png)

</details>

## Wireframes, i used Balsamiq

![Balsamiq Screen](readme-assets/wireframes/balsamiq-screen.png)


<details>
<summary>Click to expand wireframes</summary>

### Index page

 - Desktop and tablet wirefame is shared because of minimalistic design

![Index Desktop&Tablet Wireframe](readme-assets/wireframes/index-desktop.png)

 - Mobile Wireframe

![Index Mobile Wireframe](readme-assets/wireframes/index-mobile.png)


### Log In page

 - Desktop and tablet wirefame is shared because of minimalistic design

![Log In page Desktop&Tablet Wireframe](readme-assets/wireframes/login-desktop.png)

 - Mobile Wireframe

![Log In Mobile Wireframe](readme-assets/wireframes/login-mobile.png)


### Registration page

 - Desktop and tablet wirefame is shared because of minimalistic design

![Registration page Desktop&Tablet Wireframe](readme-assets/wireframes/register-desktop.png)

 - Mobile Wireframe

![Registration Mobile Wireframe](readme-assets/wireframes/register-mobile.png)

### Verify page

 - Desktop and tablet wirefame is shared because of minimalistic design

![Verify page Desktop&Tablet Wireframe](readme-assets/wireframes/verify-desktop.png)

 - Mobile Wireframe

![Verify Mobile Wireframe](readme-assets/wireframes/verify-mobile.png)

### Resend Verification page

 - Desktop and tablet wirefame is shared because of minimalistic design

![Resend Verification page Desktop&Tablet Wireframe](readme-assets/wireframes/resend-verification-desktop.png)

 - Mobile Wireframe

![Resend Verification Mobile Wireframe](readme-assets/wireframes/resend-verification-mobile.png)


### Dashboard page

 - Desktop and tablet wirefame is shared because of minimalistic design

![Dashboard page Desktop&Tablet Wireframe](readme-assets/wireframes/dashboard-desktop.png)

 - Mobile Wireframe

![Dashboard Mobile Wireframe](readme-assets/wireframes/dashboard-mobile.png)

### Settings page

 - Desktop and tablet wirefame is shared because of minimalistic design

![Settings page Desktop&Tablet Wireframe](readme-assets/wireframes/settings-desktop.png)

 - Mobile Wireframe

![Settings Mobile Wireframe](readme-assets/wireframes/settings-mobile.png)


### Profile page

 - Desktop and tablet wirefame is shared because of minimalistic design

![Profile page Desktop&Tablet Wireframe](readme-assets/wireframes/profile-desktop.png)

 - Mobile Wireframe

![Profile Mobile Wireframe](readme-assets/wireframes/profile-mobile.png)


### Add Admin page

 - Desktop and tablet wirefame is shared because of minimalistic design
 (Same as registration page)

![Add Admin page Desktop&Tablet Wireframe](readme-assets/wireframes/register-desktop.png)

 - Mobile Wireframe

![Add Admin Mobile Wireframe](readme-assets/wireframes/register-mobile.png)


### Working Now page

 - Desktop and tablet wirefame is shared because of minimalistic design

![Working Now page Desktop&Tablet Wireframe](readme-assets/wireframes/working-now-desktop.png)

 - Mobile Wireframe

![Working Now Mobile Wireframe](readme-assets/wireframes/working-now-mobile.png)


### Home Now page

 - Desktop and tablet wirefame is shared because of minimalistic design

![Home Now page Desktop&Tablet Wireframe](readme-assets/wireframes/home-now-desktop.png)

 - Mobile Wireframe

![Home Now Mobile Wireframe](readme-assets/wireframes/home-now-mobile.png)


### Add Employee page

 - Desktop and tablet wirefame is shared because of minimalistic design

![Add Employee page Desktop&Tablet Wireframe](readme-assets/wireframes/add-employee-desktop.png)

 - Mobile Wireframe

![Add Employee Mobile Wireframe](readme-assets/wireframes/add-employee-mobile.png)


### Employees page

 - Desktop and tablet wirefame is shared because of minimalistic design

![Employees page Desktop&Tablet Wireframe](readme-assets/wireframes/employes-desktop.png)

 - Mobile Wireframe

![Employees Mobile Wireframe](readme-assets/wireframes/employes-mobile.png)


### Edit Employee page

 - Desktop and tablet wirefame is shared because of minimalistic design

![Edit Employee page Desktop&Tablet Wireframe](readme-assets/wireframes/edit-employee-desktop.png)

 - Mobile Wireframe

![Edit Employee Mobile Wireframe](readme-assets/wireframes/edit-employee-mobile.png)


### Delete Employee page

 - Desktop and tablet wirefame is shared because of minimalistic design

![Delete Employee page Desktop&Tablet Wireframe](readme-assets/wireframes/delete-employee-desktop.png)

 - Mobile Wireframe

![Delete Employee Mobile Wireframe](readme-assets/wireframes/delete-employee-mobile.png)


### Nav Bar And Footer

 - Both are site-wide, desktop:

![Nav Bar And Footer Wireframe](readme-assets/wireframes/navbar-desktop.png)

 - Mobile Wireframe

![Nav Bar And Footer Mobile Wireframe](readme-assets/wireframes/navbar-mobile.png)
</details>


## Tools / Technologies

- Visual Studio Code
- HTML
- CSS
- JavaScript
- Python
- GIMP
- Microsoft Paint
- Materialize CSS 1.0.0
- Ubuntu 20.04 on WSL on Win 10 64bit
- Virtual Enviroments
- GIT, GitHub, Heroku, Heroku CLI
- MongoDB

## Database on MongoDB


For database MongoDB was the requirement.
I used <https://mongodb.com>

![MongoDB Website](readme-assets/database/atlas.png)

<details>
<summary>Click To See Database Collections</summary>

### Admin Collection

After registration of an admin details are stored in admin collection.  Please notice that email_is_verified is False and there is an verify_secret created. 

![Admin Collection Unverified](readme-assets/database/admin-unverified-database.png)

When user use correct secret code to verify the email address then email_is_verified is updated with true and secret code is deleted, for sequrity and to be able to reuse it if we have milions of registrations daily.

![Admin Collection Verified](readme-assets/database/admin-verified-database.png)

### Clock In Collection

When a employee clock-in using clock nr or clock-in card(ON NFC ONLY), details are stored on this collection. (Date, Time and Clock Nr). Because this is the most used feature, and time sensitive i decided to keep clock in and clock out in separate collections and to store the minimum required informations only here.

![Clock In Collection](readme-assets/database/clock-in.png)

### Clock Out Collection

Same as clock in but when user clock out we store in another collection all the details: Both Clock In and Clock Out and after we delete the respective entry from Clock In. This is because the user can be or clock in or clock out never both.

![Clock Out Collection](readme-assets/database/clock-out.png)

### Clocks Collection

As we said earlier when user clock out we retrieve the informations from clock in before to be deleted, first name and last name from employee collection and clock out details and we build a document in this collection with all the details to be easy accesible for furter queries.

![Clocks Collection](readme-assets/database/clocks.png)

### Employee Collection

In this collection we keep all the details of a employee when is registered by admin. Clock nr is auto generated.

![Employee Collection](readme-assets/database/employee.png)

### Index Template Collection

In this, collection are stored template settings this in only collection that have to be created at script installation.

![Index Collection](readme-assets/database/index-template.png)

</details>

## Images

- Images was taken from: <https://www.pexels.com/>



## Testing

### Responsive Design Checker (Passing all checks)

<a href="https://responsivedesignchecker.com/checker.php?url=https%3A%2F%2Fzai-clock-in-software.herokuapp.com%2F&width=1400&height=700" rel="noopener" target="_blank">Click To See</a>

### LightHouse Tests

#### Mobile Tests

<details>
<summary>Click To Expand Mobile Tests</summary>

- Index Page 

![Index Page](readme-assets/lighthouse-tests/mobile/index.png)

- Login Page

![Login Page](readme-assets/lighthouse-tests/mobile/login.png)

- Register Page

![Register Page](readme-assets/lighthouse-tests/mobile/register.png)

- Dashboard Page

![Dashboard Page](readme-assets/lighthouse-tests/mobile/dashboard.png)

- Settings Page

![Settings Page](readme-assets/lighthouse-tests/mobile/settings.png)

- Profile Page

![Profile Page](readme-assets/lighthouse-tests/mobile/profile.png)

- Working Now Page

![Working Now](readme-assets/lighthouse-tests/mobile/working.png)

- Home Now Page

![Home Now](readme-assets/lighthouse-tests/mobile/home.png)

- Add Employee Page

![Add Employee](readme-assets/lighthouse-tests/mobile/add-employee.png)

- Presence Page

![Presence Page](readme-assets/lighthouse-tests/mobile/presence.png)

- Employees Page

![Employees Page](readme-assets/lighthouse-tests/mobile/employees.png)

</details>

#### Desktop Tests

<details>
<summary>Click To Expand Desktop Tests</summary>

- Index Page 

![Index Page](readme-assets/lighthouse-tests/desktop/index.png)

- Login Page

![Login Page](readme-assets/lighthouse-tests/desktop/login.png)

- Register Page

![Register Page](readme-assets/lighthouse-tests/desktop/register.png)

- Dashboard Page

![Dashboard Page](readme-assets/lighthouse-tests/desktop/dashboard.png)

- Settings Page

![Settings Page](readme-assets/lighthouse-tests/desktop/settings.png)

- Profile Page

![Profile Page](readme-assets/lighthouse-tests/desktop/profile.png)

- Working Now Page

![Working Now](readme-assets/lighthouse-tests/desktop/working.png)

- Home Now Page

![Home Now](readme-assets/lighthouse-tests/desktop/home.png)

- Add Employee Page

![Add Employee](readme-assets/lighthouse-tests/desktop/add-employee.png)

- Presence Page

![Presence Page](readme-assets/lighthouse-tests/desktop/presence.png)

- Employees Page

![Employees Page](readme-assets/lighthouse-tests/desktop/employees.png)

</details>

### HTML Validator Tests

<details>
<summary>Click to open Validator Tests</summary>

- Index Page

Index page validator link: <a href="https://validator.w3.org/nu/?doc=https%3A%2F%2Fzai-clock-in-software.herokuapp.com%2F" rel="noopener" target="_blank">Click To See</a>

![Index Page](readme-assets/html-validator/index.png)

- Login Page

Login page validator link: <a href="https://validator.w3.org/nu/?doc=https%3A%2F%2Fzai-clock-in-software.herokuapp.com%2Flogin" rel="noopener" target="_blank">Click To See</a>

![Login Page](readme-assets/html-validator/login.png)

- Register Page

Register page validator link: <a href="https://validator.w3.org/nu/?doc=https%3A%2F%2Fzai-clock-in-software.herokuapp.com%2Fregister" rel="noopener" target="_blank">Click To See</a>

![Register Page](readme-assets/html-validator/register.png)

- Dashboard Page

Dashboard page validator link: <a href="https://validator.w3.org/nu/?doc=https%3A%2F%2Fzai-clock-in-software.herokuapp.com%2Fdashboard" rel="noopener" target="_blank">Click To See</a>

![Dashboard Page](readme-assets/html-validator/dashboard.png)

- Settings Page

Settings page validator link: <a href="https://validator.w3.org/nu/?doc=https%3A%2F%2Fzai-clock-in-software.herokuapp.com%2Fsettings%2F" rel="noopener" target="_blank">Click To See</a>

![Settings Page](readme-assets/html-validator/settings.png)

- Settings Page

Settings page validator link: <a href="https://validator.w3.org/nu/?doc=https%3A%2F%2Fzai-clock-in-software.herokuapp.com%2Fsettings%2F" rel="noopener" target="_blank">Click To See</a>

![Settings Page](readme-assets/html-validator/settings.png)

- Profile Page

Profile page validator link will throw 500 for some reason: <a href="https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fzai-clock-in-software.herokuapp.com%2Fprofile" rel="noopener" target="_blank">Click To See</a>

Page was checked by source code: 

![Profile Page](readme-assets/html-validator/profile.png)

- Working Now Page

Working Now validator link: <a href="https://validator.w3.org/nu/?doc=https%3A%2F%2Fzai-clock-in-software.herokuapp.com%2Fworking-now" rel="noopener" target="_blank">Click To See</a>

![Working Now](readme-assets/html-validator/working.png)

- Home Now Page

Home Now validator link: <a href="https://validator.w3.org/nu/?doc=https%3A%2F%2Fzai-clock-in-software.herokuapp.com%2Fhome-now" rel="noopener" target="_blank">Click To See</a>

![Home Now](readme-assets/html-validator/home.png)

- Add Employee Page

Add Employee validator link: <a href="https://validator.w3.org/nu/?doc=https%3A%2F%2Fzai-clock-in-software.herokuapp.com%2Fadd-employee" rel="noopener" target="_blank">Click To See</a>

![Add Employee](readme-assets/html-validator/add-employee.png)

- Presence Page

Presence validator link: <a href="https://validator.w3.org/nu/?doc=https%3A%2F%2Fzai-clock-in-software.herokuapp.com%2Fpresence" rel="noopener" target="_blank">Click To See</a>

![Presence](readme-assets/html-validator/presence.png)

- Employees Page

Employees validator link: <a href="https://validator.w3.org/nu/?doc=https%3A%2F%2Fzai-clock-in-software.herokuapp.com%2Femployess" rel="noopener" target="_blank">Click To See</a>

![Employees](readme-assets/html-validator/employees.png)

- Verify Page

Verify validator link: <a href="https://validator.w3.org/nu/?doc=https%3A%2F%2Fzai-clock-in-software.herokuapp.com%2Fverify" rel="noopener" target="_blank">Click To See</a>

![Verify](readme-assets/html-validator/verify.png)
</details>

### Css Tests

All CSS tests pass, error and warning is from materialize.min.css with is from Materialize. My css is error and warning free.

Validator link: <a href="https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fzai-clock-in-software.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#errors" rel="noopener" target="_blank">Click To See</a>

I did the check against my code only by code input to avoid Materialize errors.

![CSS Validator](readme-assets/css-validator/css-validator.png)

 ### JavaScript Tests

I have 2 javascripts files because i wanted some functions to be available only in index page. And like this i avoided some console logs errors.

- Index JS

![Index JS Validator](readme-assets/js-validator/index-js.png)

- Scripts Site-Wide JS

![Index JS Validator](readme-assets/js-validator/scripts-js.png)

## Deployment

- For This script you will need an account on Heroku <https://heroku.com>
For This script you will need an account on MongoDB for Database <https://mongodb.com>
- In top menu press CODE > Download ZIP or clone the project in VS Code 
- In your system you need to have to have locally installed: Python 3.10.4, pip3, GIT, Heroku Cli.
- I am using a development environment composet like: Win 10 64 Bit, Python 3.10.4, WSL - Ubuntu:20.04. On Ubuntu: VENV, GIT, HEROKU CLI. VS Code is in Windows and is accesing Ubuntu enviroment remote.
I choose to use this setup to benefit from the best tools from Windows and Ubuntu.
To setup your env like this you can use this tutorial: <https://docs.microsoft.com/en-us/windows/wsl/install>

- Once your development  env is ready and you clone the script from GitHub you need to install all requirements. This can be found in Requirements.txt file. to install fast just open a terminal in VS Code and type next comand: 

```
 pip3 install -r requirements.txt
```

This will install all the required packages.

Now go to env_example.py and copy the file and rename it to: env.py.

- Now is time to go to MongoDB site and create a database.
- After you create the database, is safe to leave it empty. All required fields will be created on first run of the software.
- Ignore any previous instructions like we need some mandatory fields in database. That was sorted in code.
- Next you need to take your database conection details and fill them in your env file.
- Go to MongoDB site click on left on database then the 3 dots next to Browse Collections and Comand line tools
- Select connect Instructions > Connect Your Application.
- Select Python and 3.12 or later  and you will get a link: 
```
mongodb+srv://username:<password>@cluster0.wiqjj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
```
- Add the link in your env.py in mongo uri field. Don't forget to replace <password>  and <myFirstDatabase> with your database name and password.
- If all is ok you should be able to run the app locally.
- Now to deploy to heroku open your terminal and type:
```
heroku login -i
```
You will be promted for your login info
```
heroku create your_app_name_here
```
 To create a new app, replacing your_app_name_here with the name you want to give your app
```
git push heroku main
```
And your app will be deployed to Heroku.

- Last steps will be to to in heroku website, access your new created app and go to settings and then scroll the page and click on Reveal Config Vars.
- Now you will need to copy your variables from env and save them in this place. Mandatory are 3 variables as you see in the image:

![Index JS Validator](readme-assets/img/heroku.png)

- Email to work you will need to add your SMTP details in same way like the app details. To learn how to get this fallow this tutorial:
<https://kinsta.com/blog/gmail-smtp-server/>

- Congratulations your app is up and running on url provided by Heroku!

## Credits / Technologies

- Materialize - For well documented css framework
- Pexels - For images
- GIMP - For Image processing
- Favicon.io - For Favicon
- Google Fonts - For Poppins font.
- Code Institute - For brilliant lessons from where i learn to do this.
- <https://unlayer.com/> - For Email Template
- <https://web.dev/nfc/> - For Briliant NFC tutorial.


## Thank you for reading. For any questions don't hesitate to contact me. Kind Regards, Ionut Zapototchi