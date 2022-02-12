# Uppsala Sotre

<p>
Uppsala Store is an online fruit and vegetable store. This online store is owned by farmers in Uppsala and its surroundings. Uppsala Store enables the farmers to sell fresh and organic food to their customers in Sweden and neighbouring countries (Norway, Denmark and Finland). Through Uppsala Store farmers can easily reach, and meet the demands of their customers. The store also creates an opportunity for customers to get fresh and organic produce at their doorstep without any hassel. Thus, the website was developed to act as a bridge between producers and consumers. It runs on Code Institute's mock terminal on Heroku.
</p>

[Here is the live version of my project](https://uppsala-store.herokuapp.com/)

![weblook of the site](/static/readmefiles/websitelook.PNG)


## User stories

| User story ID                  | As a/an   | I want to be able to..                            | So that I can…                                                               |
|--------------------------------|-----------|---------------------------------------------------|------------------------------------------------------------------------------|
| Viewing and Navigation         |           |                                                   |                                                                              |
| 1                              | Shopper   | View a list of produce                            | Buy some produce                                                             |
| 2                              | Shopper   | View produce details                              | Determine the name and  price of a produce                                   |
| 3                              | Shopper   | View produce by category                          | Easily find the produce I want to buy                                        |
| Registration and User Accounts |           |                                                   |                                                                              |
| 4                              | Site user | create an account                                 | Own an account  and view my personal profile                                 |
| 5                              | Site user | login or logout                                   | Access my  account                                                           |
| 6                              | Site user | Recover my password if I forget it                | Recover access to my account                                                 |
| 7                              | Site user | Receive email confirmation                        | Confirm that my registration was successful                                  |
| 8                              | Site user | Own a tailored user profile                       | See my order history and confirmation as well as save my payment information |
| 9                              | Shopper   | Search for a produce by its name                  | Easily find the produce I want to buy                                        |
| Purchasing and Checkout        |           |                                                   |                                                                              |
| 10                             | Shopper   | Add produce to my cart                            | Buy the produce                                                              |
| 11                             | Shopper   | Determine the quantity of a produce when shopping | Buy the right amount of each produce                                         |
| 12                             | Shopper   | See the items in my shopping cart                 | Determine the total cost of my shopping and confirm the items I am buying    |
| 13                             | Shopper   | Update the quantity of the produce in my cart     | Easily change the amount of produce I am buying                              |
| 14                             | Shopper   | Enter my payment information                      | Checkout easily                                                              |
| 15                             | Shopper   | Feel my personal  and payment information is safe | Checkout confidently                                                         |
| 16                             | Shopper   | View order confirmation after checking out        | Ensure that I have bought the right produce                                  |
| 17                             | Shopper   | Receive email confirmation after checkout         | Keep it as a record of my shoppings                                          |


## Wire frame

![Wire frame1](/static/wireframe/wireframe1.png)

![Wire frame2](/static/wireframe/wireframe2.png)

![Wire frame3](/static/wireframe/wireframe3.png)

![Wire frame4](/static/wireframe/wireframe4.png)

![Wire frame5](/static/wireframe/wireframe5.png)

![Wire frame6](/static/wireframe/wireframe6.png)

![Wire frame7](/static/wireframe/wireframe7.png)

![Wire frame8](/static/wireframe/wireframe8.png)

![Wire frame8](/static/wireframe/wireframme1.png)

![Wire framme1](/static/wireframe/wireframme1.png)

![Wire framme2](/static/wireframe/wireframme2.png)

![Wire framme3](/static/wireframe/wireframme3.png)

![Wire framme4](/static/wireframe/wireframme4.png)

![Wire framme5](/static/wireframe/wireframme5.png)

![Wire framme6](/static/wireframe/wireframme6.png)

![Wire framme7](/static/wireframe/wireframme7.png)

![Wire framme8](/static/wireframe/wireframme8.png)

# Existing Features

## User section

### Home page

* The home page welcomes the user to the website.
* The top of the page contains the logo on the left corner,
* The navigation menu and the search field in the midddle,
* My account and cart on the left corner of the page
* My account button allows the user to either register or login
* Below the navigation menu it contains a banner that motivates customers to buy more
* The Body of the home page also contains a button which takes the user to the store

![Home page](/static/readmefiles/homepage.PNG)

* The footer of the home page provides the customer with information about the facebook page (clickable) of the site as well as email subscription option so that the user can get offers
* The footer also contains a link to privacy policy of the site, when users click the link they get directed to the privacy page

![Homepage-footer](/static/readmefiles/homepage-footer.PNG)


### Sign up page

* This page contains a sign up form which allows the user to register inorder to create an account and view personal profile.
* The user signs up by providing username, email and a password.
* All of the fields are required for the user to sign up.
* The user is also required to fill the email and password twice, and if it does not match the user gets appropriate information.
* If a user tries to register with the same username or email, the user gets an appropriate message that the user or email already exists.
* At the top of the sign up form there is a link for sign in if the user has ended up in the page by mistake, this helps the user to go to the login page directly.
* The sign up form contains a sign up button which the user uses to submit the form as well as a back to login button which the user can use to go back to login page.
* Upon signing up users gets a feed back to verify their email to complete the sign up process, by responding and clicking a link sent to their registered email.

![Sign up page](/static/readmefiles/signup.PNG)


### Login page

* This page contains a sign in form which allows users to login to their account.
* The user logs in  by providing username or email and password.
* The username and password fields are required for the user to sign in.
* If the user makes a mistake while signing in, the user gets a feed back that the username or password is incorrect.
* At the top of the sign in form there is also a link for sign up page if the user has ended up in the page by mistake, upon clicking the link the user gets redirected to the sign up page.
* At the bottom of the sign in form there is a sign in button which enables the user to login.
* When users login, they get a feed back that they have successfully logged in.
* The login page also contains a button to take the user to the home page as well as a button for password reset.

![Login page](/static/readmefiles/signin.PNG)

### Store page

* In this page the user can find all the available fruits and vegetables.
* The user can also get information about the price of each produce.
* The user can determine the quantity he/she wants to buy by clicking the quantity buttons (plus or minus).
* The user can add produce to the cart by clicking the add to cart button.
* When users add a produce to the cart they get a feedback in a pop window, which informs the users how many of each produce they have added and how much they need to spend to get free delivery.
* At the bottom right corner of this page there is a button for going back to the top of the page which enables the user to easily navigate to the top of the page.

![store page](/static/readmefiles/store.PNG)

* The search field at the top allows users to search for a produce by its name.

![search](/static/readmefiles/search.PNG)

### Fruits page

* In the fruits page the user can find all the available fruits in the store.
* This page makes it easier for users to checkout what are the availabe fruits in the store.
* This page together with the search bar improves users experience of the website.
* The fruits page also contains the back to top button on its right botttom corner.

![Fruits](/static/readmefiles/fruits.PNG)

### Vegetables page

* In the vegetables page the user can find all the available vegetables in the store.
* It allows users to easily checkout the availabe vegetables in the store.
* This page together with the search bar improves users experience of the website.
* The fruits page also contains the back to top button on its right botttom corner.

![Vegetables](/static/readmefiles/vegetables.PNG)


### Contact page

* This page gives users the opportunity to leave comments or contact the site owners for any issues they want resolved.
* The contact page also enables the site owners to have an insight into how customers feel about their services and products. Thus, allowing them to improve their service.
* The contac us form contains required full name, email and comments field as well as optional phone number field.
* Once users fill out the form, they can submit it with the submit button at the bottom of the page.
* Users also get a feed back when they submit the form.

![Conact](/static/readmefiles/contact.PNG)

### Shopping cart page

* This page provides users with a summary of the produce they have added to their cart.
* The page displays the product name, price, quantity and subtotal for each produce.
* It also gives users the ability to adjust the quanity (via the quantity buttons) of the produce they have added to the cart.
* Users can use the update button to update the quantiy of their products or totally remove the produce from the cart by using the remove button.
* At the bottom right corner of this page users get a summary of the cart total, delivery price if any, and the total amount they need to pay during checkout
* It also contains butttons that allow the user to navigate to the checkout page or to continue shopping.

![Cart](/static/readmefiles/cart.PNG)


### Checkout page

* The checkout page is the page where users fill out their delivery details as well as their card details in order to complete the purchase.
* The users fill out their full name, email, telephone, street address, city, postal code and country. All of the fileds are required.
* Users also fill out their card details which is handled by Stripe payment system.
* If users are logged in they can save their details to their profile by checking the save my delivery information box, this helps users to avoid filling out their
informatin when they shop another time. Thus, improving their experience during checkout.
* In this page users also get a summary of the produce they are buying.
* If users want to update their cart content, they can do so buy clicking the update cart button at the bottom of the page.
* Once users have filled out their delivery information, card details, and checked the produce they are buying, they can place their order by
clicking the complete order button at the bottom of the page.

![Checkout](/static/readmefiles/checkout.PNG)


### Order confirmation page

* When users complete their order they are redirected to the order confirmation page.
* In this page users get information that a confirmation email of their order is sent to their email.
* They also get a summary of their order number, the date the order was made, the order details, delivery and billing information.
* At the bottom of this page there is a back to store button that allows the user to go to the store if the user want to continue shopping.

![Order](/static/readmefiles/order.PNG)


### The profile page

* In the profile page users can see their profile and they can udpate their profile information by clicking the update information button.
* The profile page is created automatically when logged in users choose to save their delivery information while completing their order.
* This page also contains the user's order history which helps the user to keep a record of their orders.
* When users click on the order number they get redirected to order confirmation page.

![Profile](/static/readmefiles/profile.PNG)


### Logout page
* when the user tries to logout, the user is asked to confirm the sign out inorder to avoid accidental logouts.
* When users logout, they get a feed back that they have sucessfully logged out.
* It also contains a button to cancel the log out process and direct the user to the home page.

![Profile](/static/readmefiles/signout.PNG)

## Site owner section

### Registered users

* The site owner can see the list of registered customers in the admin panel of the website.
* The owner of the site can delete registered users if it is needed.
* The site owner can filter registered customers based on their status.

![Users](/static/readmefiles/users.PNG)


### Orders

* The site owner can see the list of orders made by customers in the admin panel.
* The owner of the site can see a list display of the order number, the date the order was made, full name of the customer, order total, delivery cost and grand total.
* The orders are sorted by date with the latest order at the top of the list.
* The site owner can see details of the order by clicking the order number.
* The site owner can edit the details of the order or even delete it when necessary.

![Order list](/static/readmefiles/order-list.PNG)


![Order detail](/static/readmefiles/order-detail.PNG)

### Produce

* The site owner can see the list of produce in the admin panel.
* The produce section of the admin panel shows the produce name, its category (fruit or vegetable), price and its image.
* The site owner can edit details of the produce. For example change the price or remove the produce from the site when the produce is out of stock.
* The site owner can also add a new produce to the site.

![Produce](/static/readmefiles/produce.PNG)


![Produce detail](/static/readmefiles/produce-detail.PNG)


![Add produce](/static/readmefiles/add-produce.PNG)


### Contact us

* In this section of the admin panel the site owner can see a list of the comments or messages sent by customers.
* The site owner can see the customer name, email, phone number (where applicable) and comments of customers.
* The site owner can also see the details of the comments.

![Comment](/static/readmefiles/comment.PNG)


![Comment detail](/static/readmefiles/comment-detail.PNG)


## Future Features
* When time allows I would like to include login with social account.
* Give site owner a front end product management.

## Database schema

<p> The database schema includes six models. The UserProfile model has a one to one relationship with the User model created by django when a user registers to the site. It contains personal details of the user which can be used during checkout to automatically fill out the delivery details of the customer. The order model represents the order made by a customer(Userprofile) and thus a child of the Userprofile model. It contains the order number and delivery details of the customer as well as costs related to the order. The Produce model is the model for the produce in the store. It contains information about the produce such as name and price of produce. The Produce model is also a child of the catergory model which determines the category of every produce in the Produce model. The OrderLineItem model stands for an item with an order, since a shopping cart can contain many items (products) with a single order, it a child of the Order and Produce model. Thus, it connects the Order and the produce model. The contactUs model contains contact details of customers which the site owner can use to give feed back to customers comments.
</p>

![Database](/static/readmefiles/database-schema.png)
























