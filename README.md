# [The Record Store](https://the-record-store.herokuapp.com/)

This is an assignment project for [https://codeinstitute.net/](https://codeinstitute.net/). The project aims to create a webstore for selling vinyl records.

The Record Store is a ecommerce site for selling vinyl records. Customers can search for and filter products to find the records they are looking for. User accounts can be created for storing and viewing order history, creating and managing addresses to make the checkout process. Wishlists can be created and stored to user accounts so wishlist items can be quickly found to add to cart on future visits. 

## Table of Contents

1.  [UX](#ux)
	*  [Design Choices](#design-choices)
	*  [User Stories](#user-stories)
2.  [Features](#features) 
	*  [Implemented](#implemented)
3.  [Wireframes](#wireframes)
4. [Schema Design](#schema-design)
5.  [Technologies Used](#techmologies-used)
	*  [Languages](#languages)
	*  [Libraries](#libraries)
	*  [Tools](#tools)
6.  [Deployment](#deployment)
7.  [Testing](#testing)
8.  [Credits](#credits)
9.  [Disclaimer](#disclaimer)


## UX:
### Design choices
I wanted to keep the design very clean and minimal to keep with modern web design trends, I looked at many different online music stores and found a lot of the designs to be very busy and cluttered. A site that found to meet the style that I wanted was [The Record Hub](https://therecordhub.com/) so I wanted to see if I could recreate a similar design. With the design and layout decided on I wanted to find a colour scheme that was vibrant and modern. I checked through some lists of popular colour schemes of 2020 on sites like [Visme](https://visme.co/) and [Design Shack](https://designshack.net/) and found a colour scheme that Spotify had used for it's Taste Rewind promotion to be inline with what I was looking for.

![website color scheme 45](https://visme.co/blog/wp-content/uploads/2016/09/website45.jpg)




### User Stories
#### Shopper
1. As a shopper I want to be able to view all products available to purchase.
2. As a shopper I want to be able to search, sort and filter products to find a product that I want.
3. As a shopper I want to be able to see individual product details.
4. As a shopper I want add/remove products to/from my cart as well as manage quantities of products in my cart.
5. As a shopper I want add/remove products to/from a wishlist.
6. As a shopper I want to be able to pay for products with a credit card.
7. As a shopper I want to be able to checkout as a guest.
8. As a shopper I want to be able to create a user account to save details for quicker checkouts.
9. As a shopper I want to be able to create a user account to store and view my order history.
10. As a shopper I want to be able to create a user account to store and recall my wishlist. 
#### Store Owner
1. As a store owner I want to sell my products. 
2. As a store owner I want to be able to add new products to the store. 
3. As a store owner I want to be able to edit and delete existing products in the store.




## Features:
### Implemented
#### General/Home
- Navigation Bar
- Hero Carousel
- SliderJS Slides for product promotions.
- Newsletter Signup
- Emails for registration and password recovery.
#### User Profile
- Create a user account.
- Log in to a user account.
- Create addresses and store them in a user address book in the user profile.
- Edit existing addresses in the user profile address book.
- Delete addresses in the user profile address book.
- Change which address is the primary address which will auto fill in the order form.
- View order history.
#### Wishlist
- Add a product to a Wishlist.
- Remove a product from a Wishlist.
- Remove all products from a Wishlist at once.
- Add a product from the Wishlist to the cart.
- Add all Wishlist products to the cart at once.
- Save a Wishlist to a profile.
- Load a profile Wishlist on user login.
- Merge session Wishlist with the profile saved Wishlist on user login. 
#### Product Management
- Add a product to the stores database.
- Edit an existing product in the database.
- Delete a product from the database.
- Add new Genres, Artists, Labels, Formats, Colours and Tags to the database using dynamic option creation and parsing in the add product form using "Select2".
#### Store Search, Filter & Sort
- Search for products using text search, with results for a product title, artist name, label,  description and track list.
- Filter products by Price, Genre, Artist, Label, Format, Colour or Tag.
- Sort results by price or alphabetically.
#### Product Purchasing
- Add products to the cart.
- Remove a product from the cart.
- Adjust quantity of a product in the cart.
- Save and address form in the order to a user address book for use in future orders.
- Pay for an order with Stripe Payments.
- Store users orders to a user profile on checkout.
- Email order summary to customer.

## Wireframes
Below are wireframes for the site developed in [FluidUI](https://www.fluidui.com/)

- [Home)](https://github.com/Kieran-Murray-Code/CI-MS4-The-Record-Store/blob/master/wireframes/Home.PNG)
- [Products](https://github.com/Kieran-Murray-Code/CI-MS4-The-Record-Store/blob/master/wireframes/Products.PNG)
- [Product Details)](https://github.com/Kieran-Murray-Code/CI-MS4-The-Record-Store/blob/master/wireframes/Product%20Details.PNG)
- [Cart](https://github.com/Kieran-Murray-Code/CI-MS4-The-Record-Store/blob/master/wireframes/Cart.PNG)
- [Checkout](https://github.com/Kieran-Murray-Code/CI-MS4-The-Record-Store/blob/master/wireframes/Checkout.PNG)
- [Account](https://github.com/Kieran-Murray-Code/CI-MS4-The-Record-Store/blob/master/wireframes/Account.PNG)
- [Wishlist](https://github.com/Kieran-Murray-Code/CI-MS4-The-Record-Store/blob/master/wireframes/Wishlist.PNG)

## Schema Design
#### Product
| Name    | Database key | Data Type | Function |
| --- | --- | --- | --- | 
|Name | name | CharField | 
|Artist | name | ForeignKey(Artist) | 
| Label | label | ForeignKey(Label) |
| Genre | genre | ForeignKey(Genre) | 
| Format | format | ForeignKey(Format) | 
| Colour | colour | ForeignKey(Colour) | 
| Release Year | release_year | PositiveInteger |
| Price | price | Decimal | 
| Tags | tags | ManyToManyField(Tag) |
| Description | description | TextField | 
| Image | image  | ImageField |
| Tracklist | tracklist  | ArryField(CharField) |
| SKU | sku  | CharField |

#### Genre
| Name    | Database key | Data Type | Function
| --- | --- | --- | --- |
|Name | name | CharField |
|Friendly Name | friendly_name | CharField |

#### Artist
| Name    | Database key | Data Type | Function
| --- | --- | --- | --- |
|Name | name | CharField |
|Friendly Name | friendly_name | CharField |

#### Artist
| Name    | Database key | Data Type | Function
| --- | --- | --- | --- |
|Name | name | CharField |
|Friendly Name | friendly_name | CharField |

#### Label
| Name    | Database key | Data Type | Function
| --- | --- | --- | --- |
|Name | name | CharField |
|Friendly Name | friendly_name | CharField |

#### Colour
| Name    | Database key | Data Type | Function
| --- | --- | --- | --- |
|Name | name | CharField |
|Friendly Name | friendly_name | CharField |

#### Format
| Name    | Database key | Data Type | Function
| --- | --- | --- | --- |
|Name | name | CharField |
|Friendly Name | friendly_name | CharField |

#### Tag
| Name    | Database key | Data Type | Function
| --- | --- | --- | --- |
|Name | name | CharField |
|Friendly Name | friendly_name | CharField |

#### User
| Name    | Database key | Data Type | Function
| --- | --- | --- | --- |
|First Name | first_name | CharField |
|Last Name | last_name | CharField |
| Email Address | email | CharField | 
| Password | password | CharField |
| Username | password | CharField |

#### User Profile
| Name    | Database key | Data Type | Function
| --- | --- | --- | --- |
|User | user | ForeignKey |
|Primary Address | primary_address | ForeignKey  |

#### Address
| Name    | Database key | Data Type |
| --- | ---- | --- |
|User | user | ForeignKey |
|First Name | first_name | CharField |
|Last Name | last_name | CharField |
|Address Line 1 | address_line_1 | CharField |
|Address Line 2 | address_line_2 | CharField |
|Town Or City | town_or_city | CharField |
|County Or Province | county_or_province | CharField |
|Country | country | CountryField |
|Post Code Or Zip Code | post_code_or_zip_code | CharField |
|Primary Address | primary_address | BooleanField |

#### Wishlist (Subscriber)
| Name    | Database key | Data Type | Function
| --- | --- | --- | --- |
|email | email | EmailField|

#### Newsletter
| Name    | Database key | Data Type | Function
| --- | --- | --- | --- |
|User Profile | user_profile | ForeignKey(UserProfile) |
|Products | products | ManyToManyField(Product) |

#### Order
| Name    | Database key | Data Type | Function
| --- | --- | --- | --- |
|Order Number | order_number | CharField |
|User Profile | user_profile | ForeignKey(UserProfile) |
|Email | email | EmailField |
|First Name | first_name | CharField |
|Last Name | last_name | CharField |
|Address Line 1 | address_line_1 | CharField |
|Address Line 2 | address_line_2 | CharField |
|Town Or City | town_or_city | CharField |
|County Or Province | county_or_province | CharField |
|Country | country | CountryField |
|Post Code Or Zip Code | post_code_or_zip_code | CharField |
|Date | date | DateTimeField |
|Order Total | order_total | DecimalField |
|Grand Total | grand_total | DecimalField |
|Stripe PID | stripe_pid | DecimalField |

#### Order Line Item
| Name    | Database key | Data Type | Function
| --- | --- | --- | --- |
|Order | order | ForeignKey(Order) |
|Product | product | ForeignKey(Product) |
|Quantity | quantity | IntegerField |
|Line Item Total | line_item_title | DecimalField |



## Technologies Used
### Languages
-  [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
-  [CSS3](https://developer.mozilla.org/en-US/docs/Archive/CSS3)
-  [Javascript](https://www.javascript.com/)
- [Python](https://www.python.org/)

### Libraries
-  [jQuery](https://jquery.com/)
-  [Select2](https://select2.org/) - The project uses Select2 for dynamic option creation in multiselect dropdowns.
[SwiperJS](https://swiperjs.com/) .
### Frameworks
-  [Bootstrap 4](https://getbootstrap.com/) - The project used the **Bootstrap 4** for a responsive grid system.
- [Django](https://www.djangoproject.com/)

### Platforms
- [GitHub](https://github.com/)
- [Heroku](https://www.heroku.com)
- [Amazon S3 - AWS ](https://www.google.com/aclk?sa=L&ai=DChcSEwizgpPD0LvtAhUB0-0KHY7wDFcYABAAGgJkZw&ae=2&sig=AOD64_2rXXVFtm9wy-A1OqFKos_YkyuU3w&q&adurl&ved=2ahUKEwiO2IrD0LvtAhUeaRUIHeutBRkQ0Qx6BAgXEAE)
- 

### Tools
-  [Visual Studio Code](https://code.visualstudio.com/) - The project used the **Visual Studio** IDE to develop the website linked with **Github** for version control.
- [Fontawesome](https://fontawesome.com/)
-  [Autoprefixer CSS](https://autoprefixer.github.io/) - The project used the **Autoprefixer CSS** to ensure CSS compatibility with all browsers.
-  [HTML Validator](https://validator.w3.org/) - The project used the **HTML Validator** to validate and find errors in the HTML.
-  [CSS Validator](https://jigsaw.w3.org/css-validator/) -The project used the **CSS Validator** to validate and find errors in the CSS.

## Deployment
#### To deploy a live version of this site using Github the following steps are needed

#### Set Up Amazon S3 Bucket for static and media file hosting.
1. Create and Amazon AWS account.
2. Create a new S3 Bucket.
3. Configure Bucket Cors and Policy.
4. Create a User profile using IAM and give the user full access to the Bucket.
5. Create a media folder and upload the sites media files to the folder.
6. Static files will be gathered automatically on deployment to Heroku.

#### To Deploy to Heroku
1. In the [Heroku Dashboard](https://dashboard.heroku.com/apps) click on New > Create New App.
2. Give the app a name and select region.
3. Click Create app.
4. Once the app is created go to the resources tab and add the Heroku Postgres add on.
5. Once created in Deploy > Deployment Method select GitHub and connect to the app GitHub repo.
6. In Settings > Config Vars > Reveal Config Vars add AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, DATABASE_URL, EMAIL_HOST_PASS, EMAIL_HOST_USER, SECRET_KEY, STRIPE_PUBLIC_KEY,  STRIPE_SECRET_KEY, STRIPE_WH_SECRET, USE_AWS,  and give them their needed values.
7. In settings.py add the heroku app address to ALLOWED_HOSTS.
8. In settings.py add the correct values to  AWS_STORAGE_BUCKET_NAME and AWS_S3_REGION_NAME.
9. Generate a requirements.txt using `pip freeze > requirements.txt`
10. Create a new file named Procfile with no file extension, add `web: python app.py` to the file and save.
11. Push the commit and push the requirements.txt and Procfile to the GitHub. 
12. In Deploy > Manual Deploy select the master branch and click on the Deploy Branch button.

#### To deploy a local version the following steps are required.
1. Git can clone a repository using `$ git clone` https://github.com/User/Repository-To-Clone
2. Use the above command in Git Bash in your IDE such as Visual Studio Code
3. To get the URL for cloning this repository go to [The Record Store Repo](https://github.com/Kieran-Murray-Code/CI-MS4-The-Record-Store)
4. Click on the Clone or Download button.
5. Copy the link from Clone with the HTTPS section.
6. Use the command in step 1 in Git Bash, add the correct URL and hit enter.
7. You now have a local copy of the repository.
8. Setup a virtual environment with your IDE, eg `python -m venv .venv` in Vs Code.
9. Install required modules using the requirements.txt. using `pip install -r requirements.txt`.
10. Create a .env file and add the following variables to it, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, DATABASE_URL, DEVELOPMENT, EMAIL_HOST_PASS, EMAIL_HOST_USER, SECRET_KEY, STRIPE_PUBLIC_KEY,  STRIPE_SECRET_KEY, STRIPE_WH_SECRET, USE_AWS and give them their needed values.
11.  Run the app with `python3 manage.py runserver`

## Testing
Testing documented is a separate [TESTS)](https://github.com/Kieran-Murray-Code/CI-MS4-The-Record-Store/blob/master/TESTS.md) file.

## Credits
-  Code templates and workflow methods taken from Boutique Ado (Code Institute).
- Design layout ideas, media and text content taken from [The Record Hub](https://therecordhub.com/)

## Disclaimer
This website was built for educational purposes only.
