# Zai Clock in Software

Welcome, this project is 
this project is a clock in software for small business


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


