# *Dargan Health Foods* - Testing

## **Table of Contents**

- [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#javascript)
    - [Python](#python)
- [Performance](#performance)
- [Responsiveness](#responsiveness)
    - [Device Responsiveness](#device-responsiveness)
    - [Browser Responsiveness](#browser-responsiveness)
- [Defensive Design Testing](#defensive-design-testing)
- [Tested User Stories](#tested-user-stories)
    - [Prospective User](#tested-prospective-user-stories)
    - [Existing User](#tested-existing-user-stories)
    - [Site Owner](#tested-site-owner-stories)
- [Automated Testing](#automated-testing)
    - [Unittests](#unittests)
    - [Coverage Installation and Setup](#coverage-installation-and-setup)
    - [Automated Test Links and Coverage Results](#automated-test-links-and-coverage-results)
- [Bugs](#bugs)
    - [Pagination Issue](#pagination-issue)
    - [Multiple Destination Redirects](#multiple-destination-redirects)
    - [Product Discount-Price Issue](#product-discount-price-issue)
    - [Discount Code Issues](#discount-code-issues)
- [Unresolved Issues](#unresolved-issues)

---

## Code Validation

### **HTML**
[W3C HTML Validation Service](https://validator.w3.org/) was used to validate the HTML code. 

Each page was validated by URI or Direct Input.
![alt text](documentation/readme-images/html-validator-index-results.png "W3C HTML Validator results for the index page, showing no errors.")

<br>

The following table shows the pages that were checked.
No errors or warnings remain.

<br>

![alt text](documentation/readme-images/html-validator-pages-tested.png "Table of the site pages tested in the HTML Validator.")

<br>

### **CSS**

[W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate the CSS file.  

Sixteen warnings remain in total, fifteen of which are in the base.css file and one in the checkout.css file.
All of these remaining warnings relate to vendor extensions which have been deliberately added to help support
browser compatibility. 

![alt text](documentation/readme-images/css-validator-warnings.png "CSS Validator Warnings.")

<br>

No errors remain in any of the CSS files.

![alt text](documentation/readme-images/css-validator-results.png "CSS Validator Results.")

<br>

### **JavaScript**
[JSHint](https://jshint.com/) was used to validate the JavaScript used within the site.

<br>

![alt text](documentation/readme-images/jshint-results.png "JSHint Results.")

<br>

### **Python**

All *.py files were formatted with [black](https://pypi.org/project/black/) at the command line
and then checked for PEP8 compliance using [PEP8 Online](http://pep8online.com/). 

![alt text](documentation/readme-images/python-files-checked-in-pep8-online.png "Table showing the python files that were checked in PEP8 Online.")

<br>

![alt text](documentation/readme-images/automated-test-files-checked-in-pep8-online.png "PEP8 Online Test File Results.")

<br>

No errors remain within these files.

![alt text](documentation/readme-images/pep8-online-results.png "PEP8 Online Results.")

<br>

##### back to [top](#table-of-contents)
---

## Performance
[Google Chrome Developer Tools Lighthouse test](https://developers.google.com/web/tools/lighthouse) was used to test the website with regard to Performance, 
Accessibility, Best Practices and Search Engine Optimization. 

<br>

**Lighhouse Mobile Test Results for index.html**

![alt text](documentation/readme-images/lighthouse-home-mobile-results.png "Lighthouse home page mobile results.")

<br>

**Lighhouse Desktop Test Results for index.html**

![alt text](documentation/readme-images/lighthouse-home-desktop-results.png "Lighthouse home page desktop results.")

<br>

Lighthouse suggestions for improving the site's score include eliminating 3rd party 
render-blocking resources from Bootstrap, Google Fonts, Fontawesome and JQuery.
It was deemed beyond the scope of the current project to serve these critical resources inline.

![alt text](documentation/readme-images/lighthouse-eliminate-render-blocking-resources.png "Lighthouse Eliminate Render-blocking Resources suggestions.")

<br>

The remaining Lighthouse results are contained in the following tables:

![alt text](documentation/readme-images/lighthouse-all-mobile-test-results.png "Table of Lighthouse Mobile Test Results.")

<br>

![alt text](documentation/readme-images/lighthouse-all-desktop-test-results.png "Table of Lighthouse Desktop Test Results.")

<br>

##### back to [top](#table-of-contents)
---

## Responsiveness

The Dargan Health Foods site was designed using the mobile-first approach, but it was tested for responsiveness on multiple screen dimensions 
throughout the development process and after project completion using the [Google Chrome Developer Tools Toggle Device](https://developers.google.com/web/updates/2016/03/device-mode-v2) 
function and [Mozilla Firefox Developer Tools](https://developer.mozilla.org/en-US/docs/Tools).  

### Device Responsiveness

**Mobile Devices Tested**

![alt text](documentation/readme-images/responsiveness-mobile-devices-tested.png "Table of Mobile devices used for testing responsiveness.")

<br>

**Tablet Devices Tested**

![alt text](documentation/readme-images/responsiveness-tablet-devices-tested.png "Table of Tablet devices used for testing responsiveness.")

<br>

**Laptop and Desktop Dimensions Tested:**

![alt text](documentation/readme-images/responsiveness-laptop-desktop-dimensions-tested.png "Table of the laptop and desktop dimensions tested for responsiveness.")

##### back to [top](#table-of-contents)
---

<br>

### Browser Responsiveness

Each website feature, including accordions, buttons, modals, external links, hover effects etc. was manually checked within the following web browsers:
- Google Chrome
- Microsoft Edge
- Microsoft Opera
- Mozilla Firefox

<br>

#### Functions Tested As A Logged-Out User

**Home Page**

![alt text](documentation/readme-images/browser-home-functions-tested.png "Grid showing the different Home page functions tests on each browser.")

<br>

**Contact Us Page**

![alt text](documentation/readme-images/browser-contact-functions-tested.png "Grid showing the different Contact page functions tests on each browser.")

<br>

**Our Story Page**

![alt text](documentation/readme-images/browser-our-story-functions-tested.png "Grid showing the different Our Story page functions tests on each browser.")

<br>

**Registration Page**

![alt text](documentation/readme-images/browser-sign-up-functions-tested.png "Grid showing the different Registration page functions tests on each browser.")

<br>

**Login Page**

![alt text](documentation/readme-images/browser-login-functions-tested.png "Grid showing the different Login page functions tests on each browser.")

<br>

**All Products Page**

![alt text](documentation/readme-images/browser-products-functions-tested.png "Grid showing the different All Products Page functions tests on each browser.")

<br>

**Product Details Page**

![alt text](documentation/readme-images/browser-product-details-functions-tested.png "Grid showing the different Product Details Page functions tests on each browser.")

<br>

**Cart Page**

![alt text](documentation/readme-images/browser-cart-functions-tested.png "Grid showing the different Cart Page functions tests on each browser.")

<br>

**Checkout Page**

![alt text](documentation/readme-images/browser-checkout-functions-tested.png "Grid showing the different Checkout Page functions tests on each browser.")

<br>

**Checkout Success Page**

![alt text](documentation/readme-images/browser-checkout-success-functions-tested.png "Grid showing the different Checkout Success Page functions tests on each browser.")

<br>

**Blog Page**

![alt text](documentation/readme-images/browser-blog-functions-tested.png "Grid showing the different Blog Page functions tests on each browser.")

<br>

**BlogPost Page**

![alt text](documentation/readme-images/browser-blogpost-functions-tested.png "Grid showing the different BlogPost Page functions tests on each browser.")



##### back to [top](#table-of-contents)
---

<br>

#### Functions Tested as a Logged-In User

**Home Page**

![alt text](documentation/readme-images/browser-home-functions-tested-logged-in.png "Grid showing the different Home page functions tests on each browser as a logged-in user.")

<br>

**Contact Us Page**

![alt text](documentation/readme-images/browser-contact-functions-tested-logged-in.png "Grid showing the different Contact page functions tests on each browser as a logged-in user.")

<br>

**Our Story Page**

![alt text](documentation/readme-images/browser-our-story-functions-tested-logged-in.png "Grid showing the different Our Story page functions tests on each browser as a logged-in user.")

<br>

**Sign Out Page**

![alt text](documentation/readme-images/browser-sign-out-functions-tested-logged-in.png "Grid showing the different Sign Out page functions tests on each browser as a logged-in user.")

<br>

**My Account Page**

![alt text](documentation/readme-images/browser-account-functions-tested-logged-in.png "Grid showing the different Account page functions tests on each browser as a logged-in user.")

<br>

**All Products Page**

![alt text](documentation/readme-images/browser-products-functions-tested-logged-in.png "Grid showing the different All Products Page functions tests on each browser as a logged-in user.")

<br>

**Product Details Page**

![alt text](documentation/readme-images/browser-product-details-functions-tested-logged-in.png "Grid showing the different Product Details Page functions tests on each browser as a logged-in user.")

<br>

**Add Product Review Page**

![alt text](documentation/readme-images/browser-add-review-functions-tested-logged-in.png "Grid showing the different Add Review Page functions tests on each browser as a logged-in user.")

<br>

**Edit Product Review Page**

![alt text](documentation/readme-images/browser-edit-review-functions-tested-logged-in.png "Grid showing the different Edit Review Page functions tests on each browser as a logged-in user.")

<br>

**Cart Page**

![alt text](documentation/readme-images/browser-cart-functions-tested-logged-in.png "Grid showing the different Cart Page functions tests on each browser as a logged-in user.")

<br>

**Checkout Page**

![alt text](documentation/readme-images/browser-checkout-functions-tested-logged-in.png "Grid showing the different Checkout Page functions tests on each browser as a logged-in user.")

<br>

**Checkout Success Page**

![alt text](documentation/readme-images/browser-checkout-success-functions-tested-logged-in.png "Grid showing the different Checkout Success Page functions tests on each browser as a logged-in user.")

<br>

**Blog Page**

![alt text](documentation/readme-images/browser-blog-functions-tested-logged-in.png "Grid showing the different Blog Page functions tests on each browser as a logged-in user.")

<br>

**BlogPost Page**

![alt text](documentation/readme-images/browser-blogpost-functions-tested-logged-in.png "Grid showing the different BlogPost Page functions tests on each browseras a logged-in user.")

<br>

**Add Blog Comment Page**

![alt text](documentation/readme-images/browser-add-comment-functions-tested-logged-in.png "Grid showing the different Add Comment Page functions tests on each browser as a logged-in user.")

<br>

**Edit Blog Comment Page**

![alt text](documentation/readme-images/browser-edit-comment-functions-tested-logged-in.png "Grid showing the different Edit Comment Page functions tests on each browser as a logged-in user.")

<br>

##### back to [top](#table-of-contents)
---

## Defensive Design Testing

As a Logged-Out User it was attempted to access a Dargan Health Food member's account and associated pages as well as the SuperUser's Admin, Blog and Product management pages using the following urls:

* A **Profile** page: http://dargan-health-foods.herokuapp.com/profile/

  &#9745; redirects to the Login page.

* A member's **Order History** page: http://dargan-health-foods.herokuapp.com/profile/order_history/D9AC156EA79B4BDD86CA53C3D6DF077C

  &#9745; redirects to the Login page.

* A member's **Add Product Review** page: http://dargan-health-foods.herokuapp.com/products/add_review/11

  &#9745; redirects to the Login page.

* A member's **Edit Product Review** page: http://dargan-health-foods.herokuapp.com/products/edit_review/1

  &#9745; redirects to the Login page.

* A member's **Delete Product Review** link: http://dargan-health-foods.herokuapp.com/products/delete_review/2

  &#9745; redirects to the Login page.

* A member's **Edit BlogComment** page: http://dargan-health-foods.herokuapp.com/blog/edit_comment/11

  &#9745; redirects to the Login page.

* A member's **Delete BlogComment** link: http://dargan-health-foods.herokuapp.com/blog/delete_comment/2

  &#9745; redirects to the Login page.

* A member's **Change Password** page: http://dargan-health-foods.herokuapp.com/accounts/password/change/

  &#9745; redirects to the Login page.

* The site **Admin** page: http://dargan-health-foods.herokuapp.com/admin

  &#9745; redirects to the Administrative Login page.* 
  
* A superuser's **Add Product** page: http://dargan-health-foods.herokuapp.com/products/add/

  &#9745; redirects to the Login page.

* A superuser's **Edit Product** page: http://dargan-health-foods.herokuapp.com/products/edit/13

  &#9745; redirects to the Login page.

* A superuser's **Delete Product** link: http://dargan-health-foods.herokuapp.com/products/delete/12

  &#9745; redirects to the Login page.

* A superuser's **Add Blogpost** page: http://dargan-health-foods.herokuapp.com/blog/add_post/

  &#9745; redirects to the Login page. 

* A superuser's **Edit Blogpost** page: http://dargan-health-foods.herokuapp.com/blog/edit_post/3

  &#9745; redirects to the Login page. 

* A superuser's **Delete Blogpost** link: http://dargan-health-foods.herokuapp.com/blog/delete_post/1

  &#9745; redirects to the Login page. 

<br>


##### back to [top](#table-of-contents)

## Tested User Stories

<br>

#### Tested Prospective User Stories

I am a prospective Dargan Health Foods site member I want to be able to:

&#9745;	Immediately comprehend the purpose behind the Dargan Health Foods site.

Upon opening the homepage the user is presented with the Dargan Health Foods logo and brand heading
which identifies the site as an e-commerce store which sells health food. 

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-home-page-sale-banner-desktop-device.png "Screenshot of Dargan Health Foods homepage on a desktop device.")

<br>

Beneath the Sale banner the user is presented with images and links to the Latest Products,
showing them a selection of the items on offer in the store.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-home-page-mobile-device.png "Screenshot of the Home Page on a mobile device.")

<br>

Further down the same page the 'About Us' section further clarifies what the store sells.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-about-us-mobile-device.png "Screenshot of the About Us section of the Home Page on a mobile device.")

<br>

This 'About Us' section can be reached easily from any page on the site through the links provided
in the top navbar on the desktop, within the toggle dropdown navigation menu on a mobile or from
the 'Quick Links' link provided in the Footer.

Beneath the 'About Us' text is a link which brings the user to the 'Our Story' page
 where they can read about the origins of the business and its ethos.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-our-story-mobile-device.png "Screenshot of the Our Story page as it displays on a mobile device.")

<br>

&#9745; Identify where the physical store is located.

Within the footer on each page the user is presented with the shop's business address 
which is also a link bringing the user directly to the shop's location on 
[Google Maps](https://www.google.com/maps/place/Dargan+Health+Foods/@52.6663666,-8.5551142,17z/data=!3m1!4b1!4m5!3m4!1s0x485b5c109808a3ed:0x872b2c8c38046fe5!8m2!3d52.6663666!4d-8.5529255).

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-footer-desktop-device.png "Screenshot of the Find Us accordion of the Footer on a mobile device.")

<br>

This same information is contained within a dropdown-accordion, entitled 'Find Us', on mobile and portrait tablet devices.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-find-us-footer-accordion-mobile-device.png "Screenshot of the Find Us accordion of the Footer on a mobile device.")

<br>


&#9745; Easily see what products are available.

On the Home Page, site visitors, are presented with the four latest products to be added to the site.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-latest-products-desktop-device.png "Screenshot of the New Arrivals section of the Home Page on a desktop device.")

<br>

Beneath these products there is a link which takes the user to a page of All New Products added to the site.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-latest-products-mobile-device.png "Screenshot of the New Arrivals section of the Home Page on a mobile device.")

<br>

Alternatively, visitors can access site products by choosing one of the departmental titles, and their desired 'Category' choice from those displayed on the main Navbar.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-latest-products-desktop-device.png "Screenshot of the main navbar on a desktop device.")

<br>

These options are contained within the dropdown menu, accessed using the Hamburger icon, on mobile devices.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-main-menu-submenu-expanded-mobile-device.png "Screenshot of the hamburger icon menu when expanded on a mobile device.")

<br>

&#9745; Search for specific products by name or category.

As well as using the aforementioned 'Department' and 'Category' links, users can access specific products 
by entering a brand name, product-title, tag or ingredient into the search bar on the navbar.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-navbar-desktop-device.png "Screenshot of the search bar on the navbar on a desktop device.")

<br>

This input box and button appear when the magnifying-glass logo on the mobile navbar is selected.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-search-bar-expanded-mobile-device.png "Screenshot of the search bar expanded on a mobile device.")

<br>

&#9745; Sort products by category, price or alphabetically.

Users can sort the site products by category by simply choosing the desired category from the main
navigational menu or by searching for that category using the search bar.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-navbar-dropdown-expanded-desktop-device.png "Screenshot of a main nav departmental dropdown expanded on a desktop device.")

<br>

The products returned can be sorted by rating, alphabetically or by price, regardless of whether the search was 
conducted using the search bar or by selecting one of the main navigation department or category options.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-sort-dropdown-expanded-desktop-device.png "Screenshot of sort products dropdown expanded on a desktop device.")

<br>

&#9745; Be presented with an image of the product itself.

When the viewer searches for a product, department, category etc. they are presented with a range
of relevant results which show a small image of the individual products, if an image is available.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-special-offers-tablet-device.png "Screenshot of products on offer on a tablet device.")

<br>

If they viewer chooses to examine a product in more detail they can click on the product image, 
or the product title to be brought to that specific product page.  If more than one image 
exists for that product they are contained within an image carousel.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-product-image-carousel-tablet-device.png "Screenshot of a product image carousel on a tablet device.")

<br>

&#9745; Be able to read a description of a each product.

A user can read a product description on each product detail page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-product-description-mobile-device.png "Screenshot of a product's description as shown on a mobile device.")

<br>

&#9745; Be presented with nutritional information or ingredients where applicable.

On the Product Details pages for each product, if an ingredients list is available, it is to be 
found within the Details Accordion.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-product-details-accordion-expanded-mobile-device.png "Screenshot of a product's Details accordion as shown on a mobile device.")

<br>

Further information regarding allergens is to be found within the More Information accordion.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-product-more-information-accordion-expanded-tablet-device.png "Screenshot of a product's More Information accordion as shown on a tablet device.")

<br>

&#9745; Read site members’ product reviews.

Other customers' reviews of individual products can be found within the Customer Reviews accordion
on each Product Detail page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-product-customer-reviews-accordion-expanded-tablet-device.png "Screenshot of a product's Customer Reviews accordion as shown on a tablet device.")

<br>

The accordion can be accessed directly or by clicking on the Review Count link next to the product's 
star rating.

&#9745; Add products to my shopping cart with ease.

Users can use the 'Add to Cart' buttons on any Product Card to add a single unit of that 
product to their cart, without having to open that product's Details page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-products-add-to-cart-buttons-mobile-device.png "Screenshot of products with Add to Cart buttons as shown on a mobile device.")

<br>

A specific quantity of any item can be added to a user's cart using the Quantity Form and 'Add to Cart' button on the
product's Details page.  

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-quantity-form-product-details-page-desktop-device.png "Screenshot of the Quantity form and Add to Cart buttons as shown on a desktop device.")

<br>



&#9745; Be presented with a constant visual reminder of my shopping cart total and number of items already added.

The number of products within a user's cart and the cart total are displayed on the navbar at all times.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-navbar-items-in-cart-mobile-device.png "Screenshot of the Cart symbol displaying the number of items and Cart total as shown on a mobile device.")

<br>

This information is displayed within the mini-cart on the desktop navbar.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-navbar-items-in-cart-desktop-device.png "Screenshot of the Mini Cart displaying the number of items and Cart total as shown on a desktop device.")

<br>

The updated cart information is also communicated to the user using Toast messages. 
With each item added to the cart, a Success Toast appears with images of the products in the cart, their titles, and the
quantity as well as a Cart total.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-success-toast-items-in-cart-mobile-device.png "Screenshot of the Success Toast displaying the number of items and Cart total as shown on a mobile device.")

<br>


&#9745; Be able to edit my shopping cart, increasing or decreasing the quantity of a specific item or deleting it altogether, at will.

When the user opens the Cart page they are presented with a table of the items in their cart.
Each item row has a Quantity form allowing the user to increase or decrease the quantity as needed.
If they decrease the quantity to zero, the item is removed from the cart.
Alternatively, they can delete any item from the cart in one click using the individual trash-can icons
at the end of the product row.
With each adjustment of the cart the user is given feedback, the quantity updates, the line-item subtotal is
updated, as is the Cart Total and Order Total within the Summary table.
Further feedback is provided with textual messages, in green for success or in red for errors, 
which specify which item has been removed etc.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-cart-with-items-desktop-device.png "Screenshot of the Cart with items as shown on a desktop device.")

<br>

&#9745; Pay for my items using a secure credit-card payment system.

When a user is ready to pay for their items they can do so on the Checkout page.
An order summary, displaying all the items the user has in their cart, ready to purchase,
is displayed in a helpful summary table.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-checkout-desktop-device.png "Screenshot of the Checkout page as shown on a desktop device.")

<br>

Once the Billing Details form and Credit Card input has been filled out the credit card payment is handled securely by [Stripe](www.stripe.com).

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-checkout-payment-input-tablet-device.png "Screenshot of the Checkout page payment input as shown on a tablet device.")

<br>

A loading overlay and spinning icon provide visual assurance to the user that a process is taking place.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-loading-overlay-spinner-tablet-device.png "Screenshot of the loading overlay and spinning icon on a tablet device.")

<br>

&#9745; Receive immediate visual feedback when my payment has been accepted.

Upon successful processing of the payment the user is brought to the Checkout Success page.
This displays the Order details and provides the user with reassurance that their purchase has gone through.
A toast message re-affirms that a Confirmation Email is being sent to the email address provided.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-checkout-success-tablet-device.png "Screenshot of the Checkout Success page on a tablet device.")

<br>

&#9745; Receive an email confirming my purchase, order details and delivery information.

A Confirmation Email is sent to the email address provided by the customer.
This gives the customer a record of their order number and date of purchase as well as
the price paid and the delivery cost and the address the order will be shipped to. 

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-order-confirmation-email.png "Screenshot of the Order Confirmation email.")

<br>

&#9745; Read Dargan Health Foods' blog posts.

The Dargan Health Foods Blog can be accessed from any page using the link in the top navbar on the
desktop, the main dropdown menu on a mobile or from within the Quick Links in the Footer.
Additional links to the latest blog posts are provided on the Home Page.
The BlogPost card images and the BlogPost titles operate as direct links to the featured posts.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-latest-posts-desktop-device.png "Screenshot of the Latest Posts section of the home page as displayed on a desktop device.")

<br>

The main blog links bring the user to the Blog page where the user can filter posts by topic or search
the Blog for a post by keyword(s).

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-blog-tablet-device.png "Screenshot of the Blog page on a tablet device.")

<br>

A snippet of the BlogPost introductory paragraphs provides the user with further insight as to 
the contents of each before they make the final decision as to whether they want to read the full post.
For consistency, these BlogPost card images and titles also operate as links to the individual BlogPost
pages.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-blogpost-desktop-device.png "Screenshot of a BlogPost on a desktop device.")

<br>

Breadcrumbs navigation has been provided at the top of each Post to facilitate navigation within the Blog.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-blog-breadcrumbs-navigation-mobile-device.png "Screenshot of a BlogPost on a mobile device.")

<br>

Keywords assigned to the BlogPost have been rendered as Tag links below the subheading. The user can
browse other posts which share the Tag classification by clicking on the tags.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-blog-gluten-free-posts-tablet-device.png "Screenshot of posts tagged as gluten free on a tablet device.")

<br>

Ease of navigation has been further assisted through the inclusion of the Blog Search Bar
within the Search Blog accordion on each BlogPost page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-blog-search-accordion-mobile-device.png "Screenshot of the Blog Search Accordion on a mobile device.")

<br>

&#9745; Easily get in contact with the store if I have any questions.

Site visitors can easily contact the Dargan Health Foods team by filling out and submitting the
Contact Us form, links to which are provided on the desktop topnav, the mobile main dropdown 
menu and within the Footer Quick Links.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-contact-us-mobile-device.png "Screenshot of the Contact Us page on a mobile device.")

<br>

Alternatively, the store's address, email address and phone number are to be found within the Footer
'Find Us' section.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-find-us-footer-accordion-mobile-device.png "Screenshot of the Find Us accordion in the Footer on a mobile device.")

<br>
 
Users can see the most appropriate hours to contact the team by phone, or in person, by
looking at the Opening Hours provided in the Footer on every page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-opening-hours-mobile-device.png "Screenshot of the Opening Hours accordion in the Footer on a mobile device.")

<br>

&#9745; Easily locate any social media accounts connected to the site.

Social links are located in the Footer providing the user with direct access to
the company's Facebook and Instagram account pages.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-footer-mobile-device.png "Screenshot of the social links in the footer as displayed on a mobile device.")

When these links are clicked a new tab opens and the relevant page is displayed without closing the Dargan Health Foods site itself.
<br>

&#9745; Navigate through the site with ease.

A simple design structure with a fixed navbar with dropdown menus, accessible from every page of the site, provides
easy access to any page within the website. A brand logo, displayed in the top left of the screen on a desktop device,
operates as a direct link to the homepage.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-navbar-desktop-device.png "Screenshot of the Navbar on a desktop device.")

<br>

The site Footer is divided into three separate sections, which are rendered neatly as collapsed accordions on mobile devices. 
The first section/accordion provides links to the homepage, in the form of the brand header and links to 
facilitate easy contact with the Dargan's team by email or by phone. 
There is also a helpful link, which opens an external tab, showing the shop's physical location on [Google Maps](https://www.google.com/maps/place/Dargan+Health+Foods+%26+Therapy+Centre/@52.6663698,-8.5551142,17z/data=!3m1!4b1!4m5!3m4!1s0x485b5c109808a3ed:0x872b2c8c38046fe5!8m2!3d52.6663666!4d-8.5529255?shorturl=1).

Within the third section/accordion, links to commonly required site pages are 
rendered for convenience.  This provides the user with easy navigation across the site 
both at the top and bottom of the page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-footer-desktop-device.png "Screenshot of the Footer on a desktop device.")

<br>

Breadcrumbs navigation links, within the products pages and the blog pages, 
operate as a kind of secondary navigation scheme, revealing the user's location within 
that section of the website and also allowing them to jump directly to related pages along the 
path.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-breadcrumbs-navigation-links-desktop-device.png "Screenshot of the Breadcrumbs navigation links on a desktop device.")

<br>

Products and BlogPost pages are paginated for a structured browsing experience.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-pagination-mobile-device.png "Screenshot of pagination buttons on a mobile device.")

<br>

A Back-To-Top button has also been provided on these pages to allow the user to quickly return to the top of the screen
with minimal effort.

&#9745; Easily find information outlining the features that membership of the site offers to its registered users.

A section of the Home Page is devoted to encouraging new users to become a site member.
This 'Members Get More' section outlines some benefits such as membership discounts and access
to exclusive events. A call-to-action button brings to the user straight to the registration page
where they can sign up and use their new member discount code immediately to get 10% off their order.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-members-get-more-mobile-device.png "Screenshot of the Member Get More section of the Home Page on a mobile device.")

<br>

This information is reiterated on the registration page itself.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-sign-up-mobile-device.png "Screenshot of the new member promo code above the Sign Up form on a mobile device.")

<br>

Within the Shopping Cart page, non-logged-in users are provided with a link to the 'Sign In' page
so that they can apply their Promo Code and receive their discount.  This operates as a reminder to
non-registered users as to the financial benefits of becoming a Dargan's member.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-cart-with-items-sign-in-link-desktop-device.png "Screenshot of the Cart with Sign In link on a desktop device.")

<br>

On the Checkout Page, the Dargan members' smoother checkout experience is emphasised. 
Non-site members are encouraged to Sign In or to Sign Up so that they too can avoid
the time-consuming form-filling process on subsequent visits.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-checkout-sign-up-link-mobile-device.png "Screenshot of the Checkout with Sign Up link on a mobile device.")

<br>


&#9745; Easily register to become a site member.

Site visitors are presented with numerous opportunities to become site members.
On the desktop top navbar, the 'Join' link is always visible.  It brings the user directly to
the 'Sign Up' page. The 'Register' link can be found on mobile devices when the 'Account' user icon is clicked.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-account-menu-logged-out-user-expanded-mobile-device.png "Screenshot of the Account dropdown menu with Register link on a mobile device.")

<br>

Users can also access the registration page using the call-to-action button in the
'Members Get More' section of the Home Page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-members-get-more-mobile-device.png "Screenshot of the Member Get More section of the Home Page on a mobile device.")

<br>

Another 'Sign Up' link is to be found within the 'Quick Links' section/accordion in the Footer on each page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-quick-links-accordion-mobile-device.png "Screenshot of the Quick Links accordion in the Footer on a mobile device.")

<br>

Each of these registration links brings the user to the 'Sign Up' page where they can easily 
become site members by filling in the clearly labelled form and pressing the eye-catching 'Sign Up' button.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-sign-up-tablet-device.png "Screenshot of the Sign Up form on a tablet device.")

<br>

Successful submission of the form brings the user to the next stage in the registration process, email verification.
They are brought to page where they are informed that an email verification link has been sent to the address they provided.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-verify-your-email-address-message-mobile-device.png "Screenshot of the Verify Your Email Address message on a mobile device.")

<br>

Clicking the link sent in that email brings the user back to site to the following page
where they can confirm the address connected to their account and finish the registration process.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-confirm-email-address-mobile-device.png "Screenshot of the Confirm Your Email Address message on a mobile device.")

<br>

The user is then redirected to the 'Login' page with a Success Toast message.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-confirm-email-address-toast-tablet-device.png "Screenshot of the successful email confirmation toast message on a tablet device.")

<br>

##### back to [top](#table-of-contents)
---

#### Tested Existing User Stories

I am an existing Dargan Health Foods site member I want to be able to:

&#9745; Log in to the site.

Links to the 'Login' page are provided at numerous points throughout the site, however, 
they are most clearly visible on the topnav on a desktop device or within the
'Account' dropdown on a mobile device or within the 'Quick Links' section of the footer.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-navbar-desktop-device.png "Screenshot of the Sign In link on the desktop topnav.")

<br>

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-account-menu-logged-out-user-expanded-mobile-device.png "Screenshot of the Account dropdown menu with Register link on a mobile device.")

<br>

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-footer-desktop-device.png "Screenshot of the footer on a desktop device.")

<br>

All of these links bring the user directly to the 'Login' page.  Here the user is presented
with a clearly labelled form.  They can log into the site
by entering their username or email address and their password and pressing the 'Sign In' button.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-login-mobile-device.png "Screenshot of the Login page on a mobile device.")

<br>

&#9745; Navigate through the site with ease.

For the logged-in user an extra navigation link to their 'My Account' page has been provided
with the links in the topnav on the desktop, within the 'Account' dropdown on a mobile device
and in the 'Quick Links' footer section/accordion.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-vitamins-page-tablet-device.png "Screenshot of the navbar as it appears on a tablet device.")

<br>

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-account-dropdown-logged-in-mobile-device.png "Screenshot of the Log Out link within the Account dropdown on a mobile device.")

<br>

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-quick-links-accordion-logged-in-mobile-device.png "Screenshot of the Log Out link within the Quick Links accordion on a mobile device.")

<br>

&#9745; Log out of the site.

Users can log out of the site using the 'Logout' links provided in the site navbar and footer.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-account-dropdown-logged-in-mobile-device.png "Screenshot of the Log Out link within the Account dropdown on a mobile device.")

<br>

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-quick-links-accordion-logged-in-mobile-device.png "Screenshot of the Log Out link within the Quick Links accordion on a mobile device.")

<br>

These links bring the user to the 'Sign Out' page, where they can complete the process by pressing the 
'Sign Out' button.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-sign-out-mobile-device.png "Screenshot of the Sign Out page on a mobile device.")

<br>

A toast message is used to confirm that the user has been logged out.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-sign-out-toast-tablet-device.png "Screenshot of the Sign Out Success toast on a tablet device.")

<br>

&#9745; Edit my account information.

Site members have access to their 'My Account' page through the links provided in the navbar and in the footer
'Quick Links' section.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-account-dropdown-logged-in-mobile-device.png "Screenshot of the Log Out link within the Account dropdown on a mobile device.")

<br>

These links bring a site member to their personal 'My Account' page where they have access
to their 'Account Details', 'Address Book', 'Order History', 'Product Reviews' and 'Blog Comments'.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-account-my-details-tablet-device.png "Screenshot of the My Account page on a tablet device.")

<br>

On this page, within the first tabbed navigational pane, the user can choose to change their password.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-change-password-tablet-device.png "Screenshot of the Change Password page on a tablet device.")

<br>

The second tabbed navigational pane offers the user the chance to edit their default delivery address
and telephone number.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-account-my-address-book-tablet-device.png "Screenshot of the Account My Address Book tab on a tablet device.")

<br>


&#9745; Take advantage of my site membership by applying discount codes.

Site members, when logged-in, can see the special Promo Code input within their shopping cart.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-cart-logged-in-mobile-device.png "Screenshot of the Cart for a logged-in user on a mobile device.")

<br>

When the code has been successfully applied the user can see the discount that they
will receive rendered within the Cart Summary table. The discount code is rendered
as a Bootstrap badge with a small 'x' that changes when hovered over. This alerts
the user to the fact that they can remove the discount code if they so wish.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-cart-promo-code-applied-tablet-device.png "Screenshot of the Cart with Promo Code on a tablet device.")

<br>

The Promo Code and discount being applied are also rendered within the Checkout Summary.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-checkout-tablet-device.png "Screenshot of the Checkout Page with Discount Code on a tablet device.")

<br>



&#9745; Purchase my desired products using a secure online payment system.

By entering their credit card details within the Card input on the Checkout page
users can purchase their desired items.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-credit-card-input-tablet-device.png "Screenshot of the credit card input on a tablet device.")

<br>

The payment is handled securely by [Stripe](www.stripe.com).

A loading overlay and spinning icon provide visual feedback that their payment is being processed.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-loading-overlay-spinner-mobile-device.png "Screenshot of the loading overlay on a mobile device.")

<br>

Upon successful processing of the order and payment the user is redirected to the 'Checkout Success' page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-order-confirmation-page-mobile-device.png "Screenshot of the order confirmation on a mobile device.")

<br>

&#9745; Receive an order confirmation email.

The redirection to the 'Checkout Success' page and a Success Toast message inform the user that their
payment has been processed and that their order has been accepted. Text within the page
and the toast confirm the email address to which the Order Confirmation email is being sent.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-order-confirmation-mobile-device.png "Screenshot of the Success toast and order confirmation on a mobile device.")

<br>

&#9745; View my order history.

A logged-in user can see a table of their past orders within the 'My Order History' tabbed pane
on their 'My Account' page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-order-history-desktop-device.png "Screenshot of the Order History page on a desktop device.")

<br>

The order numbers on each row have been rendered in the same blue hue as other text links
within the site. This alerts the user to the fact that these numbers operate a links.
By clicking on them, the user is brought to the 'Order Confirmation' page for that order.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-past-order-confirmation-toast-mobile-device.png "Screenshot of the Past Order Confirmation toast on a mobile device.")

<br>

&#9745; Search for a product by entering a brand name, product name, allergen or other pertinent keyword into a search box within the site.

A search box is visible on the desktop navbar at all times.  The search input on a mobile appears when the magnifying-glass icon is clicked.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-search-bar-expanded-logged-in-mobile-device.png "Screenshot of a search bar on a mobile device.")

<br>

Users can search the for a product by entering a specific brand or product title into the input, or
by searching for an ingredient, tag or keyword instead.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-search-results-tablet-device.png "Screenshot of a search results on a desktop device.")

<br>

&#9745; Search for a product by department, e.g. Hair & Beauty, Vitamins & Supplements, Special Offers.

Alternatively users can use the departmental titles within the main nav to search for a broad category of products.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-department-dropdown-desktop-device.png "Screenshot of a departmental dropdown on a desktop device.")

<br>

To return all products within a Department the user can choose the relevant dropdown link,
for example, the 'All Vitamins & Minerals' option returns all of the products within the 
'Vitamins & Minerals' department.

&#9745; Sort search results, by price, alphabetically or by rating.

Users are able to sort the search results returned by rating, price or alphabetically.
This can be done by chosing the desired ordering system from the sorting dropdown select box.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-sorting-search-results-desktop-device.png "Screenshot of the sorting dropdown select on a desktop device.")

<br>

&#9745; Filter products by allergen or other pertinent tags.

Keywords/tags associated with a specific product are 
rendered as links on the Product Details page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-product-tags-desktop-device.png "Screenshot of product tags on a product details page on a desktop device.")

<br>

The user can choose to find other products associated with the 
same keyword/tag by clicking on the desired link.
They will be redirected to a page displaying those products, which
can then be sorted alphabetically, by rating or by price.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-kosher-products-tablet-device.png "Screenshot of products returned as being tagged as kosher on a desktop device.")

<br>

&#9745; See images of the product packaging.

Users are presented with an image of each product, where available, on the product cards and within the
Product Details page.
If no image is available, the user is made aware of this through the 
rendering of the 'no-image-placeholder.svg'.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-no-image-placeholder-mobile-device.png "Screenshot of a product image and the no image placeholder on a mobile device.")

<br>

Where more than one image of a product is available these are displayed, for browsing convenience,
within an image carousel on the product details page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-product-image-carousel-desktop-device.png "Screenshot of a product image carousel on a desktop device.")

<br>


&#9745; Read detailed descriptions of products.

Descriptions of the products can be found on the Product Details page for each product.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-product-details-tablet-device.png "Screenshot of a Product Details page on a tablet device.")

<br>

Further information, product ingredients and directions for usage are to be found
within the 'Details' accordion on the same page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-product-ingredients-tablet-device.png "Screenshot of the Details accordion on a Product Details page on a tablet device.")

<br>

&#9745; Read reviews of products written by site members.

Products that have been reviewed by Dargan's site members have an average star rating, rendered pictorially in 
partially or fully filled in yellow stars. Next to the stars, a Review Count shows the total number of 
customer reviews submitted so far.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-product-with-2-reviews-mobile-device.png "Screenshot of a Product Details page with reviews on a mobile device.")

<br>

This Review Count is a link that brings the user to the 'Customer Reviews' accordion where 
they can read the actual reviews.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-product-with-2-reviews-desktop-device.png "Screenshot of a Product Details page with reviews on a desktop device.")

<br>

&#9745; Leave a review of a product that I have previously purchased through the site.

Customers who have purchased a product through the site can leave a review
by navigating to the product details page for that product.
Within the 'Customer Reviews' accordion they can select the 'Leave a Review' button.
This button is only displayed if they current user has previously purchased this item.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-leave-a-review-button-mobile-device.png "Screenshot of the Leave a Review button on a mobile device.")

<br>

The customer is brought to a page with a clearly labelled form
where they can enter and submit their review.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-leave-a-review-form-tablet-device.png "Screenshot of the Leave a Review form on a tablet device.")

<br>


&#9745; Input my review easily into a user-friendly form that is straightforward to use.

The Product Review Form has a helpful label and placeholder text to instruct the user.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-leave-a-review-form-desktop-device.png "Screenshot of the Leave a Review form on a desktop device.")

<br>

The product rating simply requires the user to choose the correct number of stars from 
the dropdown select box.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-leave-a-review-form-star-rating-dropdown-desktop-device.png "Screenshot of the Leave a Review form star rating dropdown on a desktop device.")

<br>

Once all three fields have been filled the form can be posted. 

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-leaving-a-review-form-tablet-device.png "Screenshot of the a filled in review form on a tablet device.")

<br>

A Success Toast message provides feedback on the successful submission. 

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-leaving-a-review-success-toast-desktop-device.png "Screenshot of the success toast when a review is successfully posted on a desktop device.")

<br>

&#9745; Edit or delete my own reviews.

Logged-in users can edit and delete their own product review using the 'Edit' and 'Delete' links
rendered next to their review on the relevant Product Details page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-edit-delete-review-buttons-mobile-device.png "Screenshot of the Edit and Delete Review buttons on a mobile device.")

<br>

Site members also have access to these links on their 'My Account' page within the
'Product Reviews' tabbed pane. 

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-account-my-product-reviews-tablet-device.png "Screenshot of the My Account My Product Reviews tab on a tablet device.")

<br>

Clicking the 'Edit' link brings the user to the 'Edit Review' form, which has been
prefilled with the current review. The user can then alter the content as needed before
submitting the form and updating their review.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-edit-review-desktop-device.png "Screenshot of the Edit Review Form on a desktop device.")

<br>

&#9745; Be secure in the knowledge that no other user can edit or delete my reviews.

Within the 'Customer Reviews' accordion users can see that the 'Edit' and 'Delete' links are
only visible next to reviews that they themselves have submitted. Customers cannot 
alter content submitted by others.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-edit-delete-review-buttons-2-reviews-mobile-device.png "Screenshot of the Edit and Delete review buttons on a mobile device.")

<br>


&#9745; Be secure in the knowledge that measures have been put in place to prevent me from accidentally deleting one of my own reviews.

In order to prevent users from accidentally deleting their reviews, the 'Delete' link
opens a 'Delete Modal' in which the site member can 'Cancel' the action, or confirm 
that they wish to proceed by choosing the relevant button. 

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-delete-review-modal-mobile-device.png "Screenshot of the Delete Review modal on a mobile device.")

<br>

&#9745; Contact the store owner.

Site members can easily contact the Dargan Health Foods team by filling out and submitting the
Contact Us form.  Links to this page are provided on the desktop topnav, the mobile main dropdown 
menu and within the Footer Quick Links.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-contact-us-mobile-device.png "Screenshot of the Contact Us page on a mobile device.")

<br>

The Dargan Health Foods shop address, business email address and phone number are to be found within the Footer
'Find Us' section/accordion in the footer on each page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-find-us-footer-accordion-mobile-device.png "Screenshot of the Find Us accordion in the Footer on a mobile device.")

<br>
 
&#9745; Easily locate any social media accounts connected to the site.

Links to the Dargan Health Foods Facebook and Instagram accounts are to be found in the footer on every page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-footer-desktop-device.png "Screenshot of social link in the footer on a desktop device.")

<br>

&#9745; Navigate with ease to the site's blog.

Links to the Dargan's Blog are provided on the topnav of the desktop navbar,
within the main dropdown menu on the mobile navbar and within the 'Quick Links'
section/accordion of the Footer.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-blog-desktop-device.png "Screenshot of the Blog on a desktop device.")

<br>

&#9745; Search for a blog post by title or keyword.

Users can search for a BlogPost by choosing the desired topic from the
dropdown filter provided near the top of the Blog page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-blog-filter-dropdown-mobile-device.png "Screenshot of the Blog Filter dropdown on a mobile device.")

<br>

If a user wishes to search the Blog by keyword instead they can do this by entering
the term into the search bar on the main Blog page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-blog-search-bar-mobile-device.png "Screenshot of the Blog search bar on a mobile device.")

<br>

Ease of navigation within the Blog has been further assisted through the inclusion of the Blog Search Bar
within the 'Search Blog' accordion on each BlogPost page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-blog-search-accordion-mobile-device.png "Screenshot of the Blog Search Accordion on a mobile device.")

<br>

In a similar fashion to the keyword tags on the products pages, users can click on
the BlogPost tags to find other posts which share that classification

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-blog-post-with-tags-tablet-device.png "Screenshot of a blog post with tags on a tablet device.")

<br>

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-blog-gluten-free-posts-desktop-device.png "Screenshot of the blog posts tagged as gluten free on a desktop device.")

<br>

Breadcrumbs links allow users to jump to the related topic page or the main Blog page directly from a BlogPost.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-blog-breadcrumbs-navigation-desktop-device.png "Screenshot of the Blog breadcrumbs navigation on a desktop device.")

<br>

&#9745; Comment on a blog post.

Beneath each blog post, within the 'Comments' accordion, there is a 'Leave a Comment' button.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-blog-leave-a-comment-button-mobile-device.png "Screenshot of the Leave a Comment button mobile device.")

<br>

This brings users to the Blog Comment form, which allows them to input their comment
into a simple text field and 'Upload' it.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-blog-comments-form-tablet-device.png "Screenshot of the Add Blog Comment form on a tablet device.")

<br>

When the user uploads their comment successfuly they are given feedback in the form of a 
Success Toast message.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-success-toast-blog-comment-tablet-device.png "Screenshot of success toast when submitting blog comment on a tablet device.")

<br>

&#9745; Edit or delete my own comments.

Each site member has the ability to edit or delete their own Blog Comments.

'Edit' and 'Delete' links are to be found next to the individual comments beneath 
the related BlogPost. These are visible solely to the creator of the comment in question.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-blog-comments-mobile-device.png "Screenshot of Blog Comments on a mobile device.")

<br>

Alternatively members can access all of their Blog Comments and the associated 'Edit' and 'Delete' links
from within their 'My Account' page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-account-my-blog-comments-tablet-device.png "Screenshot of My Blog Comments section of the Account page on a tablet device.")

<br>

The 'Edit' link brings the user to the Edit Comment form where they can change their comment.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-edit-blog-comment-tablet-device.png "Screenshot of Edit Blog Comment page on a tablet device.")

<br>

The 'Delete' link opens a Delete Modal asking the user to confirm their decision to delete their
comment.  If they choose to continue with the action by pressing the 'Delete' button, 
the comment is deleted from the database.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-delete-blog-comment-modal-mobile-device.png "Screenshot of Delete Blog Comment modal on a mobile device.")

<br>



##### back to [top](#table-of-contents)
---

#### Tested Site Owner Stories

As the owner of Dargan Health Foods website I would like to:

&#9745;	Provide users with an effective and user-friendly platform where they can see what products Dargan's have to offer.

Site visitors can see images of the products on the site within the product cards displayed
in the 'New In' section of the homepage and on the different 'Products' pages,
whether they choose to browse the store by department, category, tag or to search 
for a keyword or by brand. 

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-organic-products-store-owner-desktop-device.png "Screenshot of a the Organic search results page on a desktop device.")

<br>

&#9745; Provide site users with a straightforward online shopping experience.

The high-quality images provided, where available, allow the user to quickly visually identify the products.
If they recognise them as the product they require, an 'Add to Cart' button allows
them to add a single unit of that product to their shopping cart immeditately 
without the need to opening the individual 'Product Details' page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-all-products-store-owner-desktop-device.png "Screenshot of a the All Products page on a desktop device.")

<br>

&#9745; Provide visitors with visually appealing images of the products on offer.

Where more than one image is available the user can easily scroll through them using the
previous and next controls on the image carousel.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-product-image-carousel-store-owner-desktop-device.png "Screenshot of a product image carousel on a desktop device.")

<br>

Ribbons on certain product cards alert the user to products which are currently on offer.
The regular product price is displayed in muted strikethrough text alongside the sale price
allowing the user to see at a glance the value of the potential saving.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-products-store-owner-desktop-device.png "Screenshot of the products page on a desktop device.")

<br>


&#9745; Provide visitors with information about the products, such as their ingredients/nutritional information 
(where applicable), so that they can make more informed choices when choosing their products.

Each 'Product Details' page provides site visitors with a general description of that product.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-product-description-store-owner-mobile-device.png "Screenshot of a product description on a mobile device.")

<br>

If they user wishes to access more information, including the product ingredients and 
directions for consumption they can do so by opening the 'Details' accordion
on the same page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-product-ingredients-store-owner-tablet-device.png "Screenshot of a product ingredients list on a tablet device.")

<br>

&#9745; Provide site users with an easy way to add their desired product to their cart.

The eye-catching 'Add to Cart' buttons on the product cards allow users to add a single
unit of the desired item to their cart immediately without having to open the 'Product Details' 
page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-add-to-cart-buttons-store-owner-mobile-device.png "Screenshot of the 'Add to Cart' buttons on a mobile device.")

<br>

If the user wishes to add more than one unit of the item to their cart they can 
do so on the 'Product Details' page using the quantity input and the 'Add to Cart' button.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-product-details-quantity-input-store-owner-tablet-device.png "Screenshot of the quantity input on a tablet device.")

<br>

Users can also increase or decrease the quantity of any item in their shopping cart
using the quantity controls within the 'Cart' page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-cart-quantity-controls-store-owner-tablet-device.png "Screenshot of the quantity controls in the Cart on a tablet device.")

<br>


&#9745; Provide users with a visual representation of their cart total and the number of products already added, visible on all screens.

Users can see the number of items currently in their cart and the current cart total
on the site navbar at all times.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-cart-icon-with-items-mobile-device.png "Screenshot of the cart icon with items on a mobile device.")

<br>

On desktop devices this has been rendered as a 'Mini Cart'.  The cart icon and total allow
the user to navigate to the 'Cart' page. The 'Checkout' button allows them to skip this 
step and go directly to the 'Checkout' page if they wish.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-cart-icon-with-items-desktop-device.png "Screenshot of the cart icon with items on a desktop device.")

<br>


&#9745; Provide users with an updated total when they add or remove products from their cart.

When users add items to their cart the cart total and number of items within their cart
are updated on the navbar.  Further confirmation of the addition is provided in the 
form of a Success Toast message.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-success-toast-items-mobile-device.png "Screenshot of the success toast message on a mobile device.")

<br>

If a user removes or updates the quantity of an item from within the 'Cart' page the 
navbar total and number of items is updated, the lineitem subtotal is changed and 
the cart 'Summary' table is updated.  A textual message is displayed on screen 
providing further visual confirmation of the action performed.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-update-cart-message-mobile-device.png "Screenshot of the cart update message on a mobile device.")

<br>


&#9745; Provide users with an easy-to-use and secure online payment process.

Dargan Health Foods secure payment system is provided by [Stripe](www.stripe.com).
Users can purchase their desired products by completing the clearly labelled
'Billing Details' form and entering their credit card details into the Stripe input.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-stripe-input-filled-mobile-device.png "Screenshot of the Stripe input on a mobile device.")

<br>

&#9745; Provide site users with product reviews written by site members.

Product reviews left by Dargan Health Foods members can be read by any site visitor.
The average score for a product is displayed pictorially in partially or fully 
filled-in stars on the 'Product Details' page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-star-rating-desktop-device.png "Screenshot of a product's star rating on a desktop device.")

<br>

The 'Review Count' not only lets the user know how many reviews the rating is out of, but
it also operates as a link, opening the 'Customer Reviews' accordion and bringing the 
user to that part of the page so that they can read the reviews.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-customer-reviews-accordion-desktop-device.png "Screenshot of the 'Customer Reviews' accordion on a desktop device.")

<br>

&#9745; Provide site members with a user-friendly way to share their own reviews of products, edit those reviews or delete them as they see fit.

Dargan Health Foods site members can leave reviews of products that they have purchased
by clicking on the 'Leave a Review' button which is visible at the 
top of the 'Customer Reviews' accordion on the 'Product Detail' page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-leave-a-review-button-desktop-device.png "Screenshot of the 'Leave a Review' button on a desktop device.")

<br>

This brings the user to a well-labelled, easy-to-fill-out form.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-product-review-form-desktop-device.png "Screenshot of the 'Product Review Form' on a desktop device.")

<br>


&#9745; Present the reviews in a visually appealing format.

Product review titles are prefixed with a pictorial representation of the product 
rating in stars which allow users to see each customer's score at a glance.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-customer-reviews-tablet-device.png "Screenshot of the 'Customer Reviews' accordion on a tablet device.")

<br>

A member's star ratings are also rendered within the
'My Product Reviews' tabbed navigational pane on their 'My Account' page.
This table provides users with a quick overview of their reviews and 
product ratings as well as providing them with links to those reviews
and the ability to edit or delete their own content.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-my-account-product-reviews-tablet-device.png "Screenshot of the 'My Product Reviews' tabbed pane on a tablet device.")

<br>


&#9745; Provide site members with the ability to search the site for a 
specific product by entering the name or the brand into a search box within the site.

Users can use the search bar on the navbar to search for a product by 
title, brand or keyword.  This search bar is visible at all times on the 
desktop navbar.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-search-bar-and-results-tablet-device.png "Screenshot of a search for a product brand on a tablet device.")

<br>

This search bar appears once the magnifying-glass icon on the mobile
navbar has been clicked.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-search-bar-and-results-mobile-device.png "Screenshot of a search for a keyword on a mobile device.")

<br>

&#9745; Enable sorting of search results.

Search results, whether conducted using the search bar or using the departmental and 
category links, can be sorted alphabetically or by price or rating using the 
'Sort by...' dropdown select box.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-sort-dropdown-desktop-device.png "Screenshot of the 'Sort' dropdown on a desktop device.")

<br>


&#9745; Encourage more users to sign up to become members of the Dargan community by creating a professional-looking website that is intuitive to use. 

Site visitors are encouraged to become site members. 
There is a section of the homepage, entitled 'Members Get More'
which outlines some of the benefits of joining the site.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-members-get-more-desktop-device.png "Screenshot of the 'Members Get More' section on a desktop device.")

<br>

The financial benefits of being a Dargan's member is emphasised 
on the 'Cart' page with the inclusion of a 'Sign In' link and
reminder to visitors that site members can avail of discounts 
by applying Promo Codes to their Cart.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-cart-sign-in-link-tablet-device.png "Screenshot of the 'Sign In' link on a tablet device.")

<br>

&#9745; Provide prospective members with the ability to sign-up easily.

Links to the site registration page are found within the navbar and footer on 
every page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-logged-out-navbar-desktop-device.png "Screenshot of the navbar on a desktop device.")

<br>

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-logged-out-footer-desktop-device.png "Screenshot of the footer on a desktop device.")

<br>
In addition to these very visible reminders, further links have been provided
within other site pages at strategic points in order to facilitate ease of registration.
For example, when a user is on the 'Checkout' page they are
provided with multiple opportunities to sign up in order to 
take advantage of a faster checkout process in the future.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-checkout-sign-up-links-tablet-device.png "Screenshot of the 'Sign Up' links in the Checkout on a tablet device.")

<br>

Any 'Sign Up' link brings the user to the clearly labelled 'Sign Up Form'.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-sign-up-tablet-device.png "Screenshot of the 'Sign Up Form' on a tablet device.")

<br>

Once the form has been filled out and submitted the user is informed that they
have been sent an email in order to confirm that the email address they
provided is legitimate.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-verify-your-email-desktop-device.png "Screenshot of the 'Verify Your Email Address' page on a desktop device.")

<br>

When the user follows the link sent to their email address they simply
have to press a button to confirm that their address to complete the sign-up process.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-confirm-your-email-desktop-device.png "Screenshot of the 'Confirm Your Email Address' page on a desktop device.")

<br>


&#9745; Encourage more visitors to follow the site on social media and thereby raise the profile of the store.

Dargan's have an active social media presence on Facebook and on Instagram.
Visitors to the website are alerted to this presence through the inclusion
of the aforementioned platform's icons in the footer on every page.
Clicking on these icons opens a new tab within the user's browser and 
brings them to the Dargan's account page on the selected social media platform.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-footer-tablet-device.png "Screenshot of the footer on a tablet device.")

<br>



&#9745; Provide visible contact details so that all site visitors can contact the store with ease.

The Dargan Health Foods email address, phone number and postal address are provided
on every page within the footer. 

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-logged-out-footer-desktop-device.png "Screenshot of the footer on a desktop device.")

<br>

Store opening times are also displayed here for convenience.

If the user however, wishes to contact the store from within the website they can
do so using the 'Contact Us Form' which is found by following the links provided in the
footer or within the navbar.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-logged-out-navbar-desktop-device.png "Screenshot of the navbar on a desktop device.")

<br>

The form itself has helpful placeholder text which clarifies what each field is for.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-contact-us-form-tablet-device.png "Screenshot of the 'Contact Us Form' on a tablet device.")

<br>

&#9745; Be able to add new products to the online website with ease.

The Store Owner can add a new product to the website using the 'Add Product'
link within the specially extended Superuser's navbar.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-superuser-account-dropdown-tablet-device.png "Screenshot of the superuser 'Account' dropdown on a tablet device.")

<br>

Alternatively the 'Add Product' link can be found within the 'Quick Links' section/accordion
in the Superuser's footer.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-superuser-footer-tablet-device.png "Screenshot of the superuser footer on a tablet device.")

<br>

These links bring the Superuser to a clearly labelled form
where they can add in the relevant product details before uploading 
the new product to the site.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-superuser-add-product-form-tablet-device.png "Screenshot of the superuser 'Add a Product' form on a tablet device.")

<br>

To make the process as straightforward as possible,
the 'Category' 'Brand' and product 'Tag' fields are presented
as dropdown select boxes.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-superuser-add-product-category-dropdown-desktop-device.png "Screenshot of the superuser category dropdown on the 'Add a Product' form on a desktop device.")

<br>

&#9745; Edit existing product information with ease.

When it comes to editing a product's details the Superuser
has access to this functionality through the 'Edit' links
which are rendered on each 'Product Details' page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-superuser-edit-product-link-desktop-device.png "Screenshot of the superuser 'Edit' product link on a desktop device.")

<br>

This brings the Superuser to a pre-filled form where
they can edit the current information before saving their alterations.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-superuser-edit-product-form-desktop-device.png "Screenshot of the superuser 'Edit Product Form' on a desktop device.")

<br>



&#9745; Indicate to customers when a product is out of stock.

&#9745; Delete and/or discontinue products that are no longer available, removing their images and information from the website.

Delete functionality is provided to Superusers through the provision
of 'Delete' links which are to be found on each 'Product Detail' page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-superuser-delete-product-link-desktop-device.png "Screenshot of the superuser 'Delete' product link on a desktop device.")

<br>

A 'Delete Modal' ensures that products are not accidentally deleted in this manner.
In order to remove the product from the database the Superuser must confirm their
decision by choosing the 'Delete' button.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-superuser-delete-product-modal-desktop-device.png "Screenshot of the superuser 'Edit Product Form' on a desktop device.")

<br>

If a product has been discontinued, rather than deleting if from the 
database, a 'Discontinued' field has been provided.  This allows the
Superuser to remove a product from view within the site by selecting
the 'Yes' option in the 'Discontinued' dropdown on the 'Edit Product
Form'.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-superuser-discontinued-dropdown-desktop-device.png "Screenshot of the superuser 'Edit Product Form' on a desktop device.")

<br>


&#9745; Easily add a new blog post to the site blog.

The link to the Superuser's 'Add Blog Post' form is also to be
found within the 'Account' dropdown on a mobile device, within the top 
navbar on a desktop device and within the 'Quick Links' section/accordion
in the site footer on every page.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-superuser-quick-links-accordion-mobile-device.png "Screenshot of the superuser 'Quick Links Accordion' on a mobile device.")

<br>

A new blog post can be added by filling out the clearly labelled form
and pressing the 'Add Blog Post' button.

![alt text](documentation/readme-images/tested-user-stories-screenshots/screenshot-superuser-add-blog-post-form-mobile-device.png "Screenshot of the superuser 'Add Blog Post Form' on a mobile device.")

<br>


##### back to [top](#table-of-contents)
---

## Automated testing

### Unittests

Django's testing framework was used to create automated tests for the project.

A tests directory was added to each app.
Within these directories individual files were created to test the app's views, models and forms.

In order to run specific tests, the following command can be used:
```
python3 manage.py test <app_name>.tests.<test_name>
```

To run all the tests use the command:
```
python3 manage.py test
```

[Coverage](https://coverage.readthedocs.io/en/coverage-5.5/)
was used to identify the percentage of code covered by the tests.

<br>

##### back to [top](#table-of-contents)
---

### Coverage Installation and Setup

Install the package using pip.
```
pip3 install coverage
```

Add this new dependency to your requirements.txt file.
```
pip3 freeze > requirements.txt
```

Run all the tests within in a specific app using the following command:
```
coverage run --source=<'app_name'> manage.py test
```

To generate a report of the results in the terminal use:
```
coverage report
```

Alternatively, a directory containing HTML versions of the report sections 
can be created by typing:
```
coverage html
```
The report can then be viewed in a web browser using the command:
```
python3 -m http.server
```
and selecting the 'htmlcov/' directory.

<br>

##### back to [top](#table-of-contents)
---

### Automated Test Links and Coverage Results

|Test Files                                         |   Tests                                                   | Coverage Result |
|---------------------------------------------------|-----------------------------------------------------------|----------|
|[Blog Forms](blog/tests/test_forms.py)             |   BlogPostForm and BlogPostCommentForm validation.        |100%|
|[Blog Models](blog/tests/test_models.py)           |   Topic, BlogPost, BlogPostTag and BlogPostComment Model creation and string methods. That BlogPost titles are slugified.|98%|
|[Blog Views](blog/tests/test_views.py)             |   All blog posts and individual blogpost views.           |28%|
|[Cart Forms](cart/tests/test_forms.py)             |   DiscountCodeForm creation.                              |100%|
|[Cart Models](cart/tests/test_models.py)           |   DiscountCode Model creation and string method.          |100%|
|[Cart Views](cart/tests/test_views.py)             |   Calculating cart subtotal, testing the cart view, add to cart functionality, and adjusting and removing items from the cart |21%|
|[Checkout Forms](checkout/tests/test_forms.py)     |   OrderForm creation and required fields                  |100%|
|[Checkout Models](checkout/tests/test_models.py)   |   Order and OrderLineItem model creation and string methods. Also test the OrderLineItem get_total_lineitem_price method.|94%|
|[Checkout Views](checkout/tests/test_views.py)     |   Testing checkout and checkout success view              |27%|
|[Home Forms](home/tests/test_forms.py)             |   NewsletterSubscription and Contact form validation and required fields.|100%|
|[Home Models](home/tests/test_models.py)           |   NewsletterSubscription model creation and string method.|100%|
|[Home Views](home/tests/test_views.py)             |   Testing index, our_story and  contact views.            |46%|
|[Products Forms](products/tests/test_forms.py)     |   ProductForm and ProductReviewForm creation and validation.|100%|
|[Products Models](products/tests/test_models.py)   |   Brand, Department, Category, Tag, Product, ProductImage, ProductTag and ProductReview model creation and string methods.|100%|
|[Products Views](products/tests/test_views.py)     |   Testing form fields, products, product detail, add product and edit product view, adding a product, and sort and filter functionality|25%|
|[Profiles Forms](profiles/tests/test_forms.py)     |   DargansCustomSignupForm and UserProfileForm creation and validation. |81%|
|[Profiles Models](profiles/tests/test_models.py)   |   UserProfile and DiscountCode2User model creation and string methods.|100%|
|[Profiles Views](profiles/tests/test_views.py)     |   Profile view when a user is logged in, and not logged in. If successful, check that the correct template was rendered. |68%|

<br>

##### back to [top](#table-of-contents)
---

### Overall Automated Test Coverage

For the purposes of a MVP at least 55% of each app is covered by automated tests.
It is hoped to continue to increase the test coverage to as close to 100% as possible.

|App Name           |Percentage of App Code Currently Covered by Tests     |
|:------------------|:-------------------:|
|Blog               |67%                |
|Cart               |55%                |
|Checkout           |58%                |
|Home               |81%                |
|Products           |70%                |
|Profiles           |89%                |

<br>

##### back to [top](#table-of-contents)
---

## Bugs

### Pagination Issue
[Pagination]((https://github.com/nualagr/dargan-health-foods/commit/7b8b1e0fc9afd4d0f8b39b69611bc38c8679ff28)) was applied to the products.html page and initially worked correctly.  However, once filtering of products 
by search criteria was implemented, the pagination 'previous' and 'next' buttons
brought the user to page one or three of the products.html page, rather than the page associated with the chosen queryset. 
This problem was put to one side. Filtering of products by category and department was implemented. Then sorting of 
results was developed. Once filtering by tag had been put in place the issue of pagination was again approached.
At first 
```
{{ request.get_full_path }}
```
was used to get the url and feed it to the 'next' and 'previous' pagination buttons, however this was unsuccessful since this 
url contains not only the search criteria etc., but also '?page=1'. Therefore, when navigating from 'page=2' to 'page=1', 
the former remained within the url, invalidating it. 

The application of a [custom template tag](https://github.com/nualagr/dargan-health-foods/commit/dd1d2fddb32e018da0371fd252210762fe3eb062)
succeeded in rectifying the issue.  In the template the custom template tag 'current_query_url' 
is called and it is passed three arguments, the 'page' keyword, the current page number and the current url.
```
href="{% current_query_url 'page' page_obj.previous_page_number request.GET.urlencode %}" aria-label="Link to Previous Page">
```
Within the template tag the new page-number element of the url is reconstructed from the 'page' 
keyword and the new page_number value. Then the encoded url is split into its constituent parts at the '&'.
The page-number element is filtered out and the remaining query element(s) are reattached using an ampersand.
Finally the query elements of the url are connected with the new page number element and returned to the template.

``` {.python3}
@register.simple_tag
def current_query_url(key, value, urlencode=None):
    # Isolate the page number in the format ?page=1
    url = "?{}={}".format(key, value)
    if urlencode:
        queries = urlencode.split("&")
        # Isolate queries from page number
        filtered_queries = filter(lambda q: q.split("=")[0] != key, queries)
        # Join queries using the ampersand
        encoded_queries = "&".join(filtered_queries)
        # Reattach the queries to the page number
        url = "{}&{}".format(url, encoded_queries)
    return url

```

This succeeded in bringing the user to the next/previous page of the results queryset, including 
the chosen category, department, tag or search term and sorting choice.

Pagination caused issues [again](https://github.com/nualagr/dargan-health-foods/commit/80532381676ebbe2f619fbffd42b5d5f0add8c97) 
once the site had been populated with a significant number of products as
the number of page links resulted in horizontal overflow, particularly when viewed on mobile devices.
An answer posted on [StackOverflow](https://stackoverflow.com/questions/41131802/django-paginator-page-range-for-not-displaying-all-numbers)
suggested limiting the number of links being rendered within the template.
An 'if' 'elif' 'else' block was added to the pagination.html include to limit the number 
of page numbers being rendered to +-3 on either side of the active page number.
```
 {% for i in page_range %}
    {% if page_obj.number == i %}
        <li class="page-item active">
            <span class="page-link">{{ i }}
                <span class="sr-only">(current)</span>
            </span>
        </li>
    {% elif i <= page_obj.number|add:3 and i >= page_obj.number|add:-3 %}
        <li class="page-item">
            <a class="page-link" href="{% current_query_url 'page' i request.GET.urlencode %}" aria-label="Link to Page {{ i }}">{{ i }}</a>
        </li>
    {% else %}
    {% endif %}
{% endfor %}
```
This removed the horizontal overflow, but is not an ideal solution as it was not immediately obvious
to the viewer that the page range does not reflect the total number of pages returned.

<br>

### Multiple Destination Redirects
This issue arose in relation to two different pages, the Edit Product Review 
page and the Edit BlogPost page.  Links to these pages exist in multiple locations within the site.
Initially the redirects, upon submission of the forms, were hardcoded to a single location. 
If the user edited their product review they were redirected to the product page, 
even if they had clicked the 'Edit' button on their Profile page.
This was less than satisfactory, from a user-experience point of view.
[In order to redirect users to the page from which they had initially come](https://github.com/nualagr/dargan-health-foods/commit/0ee02100805b0a999e9a9fac397cd26c41b13bf3),
it was necessary to capture the referring page url from the HttpRequest.META, 
which is a dictionary containing all the HTTP headers including the HTTP_REFERER. 
As this value changes to the current url upon the submission of the form
it was necessary to assign the referring url, with the GET request, to a hidden input on the EditReview form.
```
<input type="hidden" value="{{ request.META.HTTP_REFERER }}" name="previous_page_url">
```
The referring url is now posted along with the review to the edit_review view where an 'if' 'else'
block checks for the existence of the substring "profile" within the url before redirecting to the 
appropriate page.
``` {.python3}
# If the user got to the edit review page from their profile
# Redirect them back to their profile page.
if "profile" in previous_page_url:
    return redirect(reverse("profile"))
else:
    # Redirect to the Product's Details Page
    return redirect(reverse("product_detail", args=[product.id]))
```

<br>

### Product Discount Price Issue
When it came to applying a [discount to individual products](https://github.com/nualagr/dargan-health-foods/commit/506f2f19c369db6eba3a474022047e26b5cc1ae2),
for the purposes of an MVP, a 'discount_price' field and a Boolean 'on_offer' field were added to the Product model. 
This allowed SuperUsers to mark individual product prices down from within the admin panel. 
This new structure was then reflected in the OrderLineItem Model where the subtotal for each lineitem is calculated. 
An issue arose relating to a User's past orders however.  The Order model accesses the 'product.price' through a Foreign Key to the Product model.
This points to the price for that product, as it appears, currently, in the database. 
The Order, however, needed to reference the price, as it existed, when the order was originally placed.
This original price had been, and still is, stored in the Order model within the json string of the original_cart.
To facilitate easier access to this vital piece of information, a new field, 'product_price_paid', was added to the OrderLineItem model.
This value is now set when the OrderLineItem is saved. 
It is this field that is now accessed and displayed within each order on the profile.html 'My Orders' tab.

<br>

### Discount Code Issues
The addition of Discount Codes to the project required revision of many elements of the payment process.

At first, a very simple [DiscountCode model](https://github.com/nualagr/dargan-health-foods/commit/c9445ca3d1c48bb004ce65434aaf856e3cfdcad2) 
of only two fields was used. This consisted of the promo code and the associate percentage discount to be applied.
After reading Kim Salazar's article ["Applying Discounts and Ecommerce Websites"](https://www.nngroup.com/articles/applying-discounts/) it became clear
that, from a user-experience point-of-view, it would be best to allow site users to apply this code within the Cart rather than making them wait
until they were on the Checkout page. This approach enables people to check that the discount code is valid before they enter any personal information 
and also allows the total to be updated appropriately early in the process.
A DiscountCodeForm, based on the DiscountCode model was created and rendered on the cart.html page. On submission of this form, the discount code, 
if valid, is stored in the Session Cookie.

The discount_amount is then calculated and applied to the cart 'total' within the cart_contents context.
The discount code object is saved in a variable, discount_code, and added to the context dictionary so that it is globally available within the different templates.

Within the 'checkout' view the discount code object ID is obtained from the session cookie.
The corresponding DiscountCode object is attached, as a ForeignKey field, to the Order before it is saved to the database.
Then when .save() is called on the Order, the update_total() method is called and the discount applied.

To be able to provide the user with visible feedback on the financial benefit of the addition of their promo code, 
a new variable, ['total_before_discount'](https://github.com/nualagr/dargan-health-foods/commit/cdac94bafada5d89e5310a452a4785b2cbb578fe)
was created within the cart_contents context.  'If' 'else' statements were added to the checkout_success.html page to render the discount code and the amount
of money discounted, providing the user with confirmation that they received their discount.  

Within the '_send_confirmation_email()' function in the webhook_handler two new variables were created to store the discount code and amount discounted.
These are set to empty strings if no discount code was used. Otherwise, the discount code and amount discounted are printed within the email providing
customers with a confirmation that their promo code had been applied and that they had received the discount they expected.

Logic then had to be applied to [handle the discount when orders are created within the webhook](https://github.com/nualagr/dargan-health-foods/commit/fabfac039b94966cbd99fc3b59e166e2c4d5bd44). 
This process is triggered when errors occur during the checkout process, such as the browser being closed before the Order has been created in the database.
In the cache_checkout_data() function in the checkout/views.py a json string of the discount code was attached to the Payment Intent metadata. 
Within the handle_payment_intent_succeeded() function this is unpacked and the associated DiscountCode object located in the database. 
This object can then be linked to the discount_code ForeignKey field on the newly created Order.
This ensured that Orders created in this manner, within the webhook, now correctly reflect the discount applied by the user in the Cart.

An issue arose in relation to this however as [exceptions were raised when no discount code had been applied to the Order being created in the webhook](https://github.com/nualagr/dargan-health-foods/commit/0b92b6e7594f0881dc2f2cb0d934ddf8b95511e7).
Different solutions, suggested by [StackOverflow](https://stackoverflow.com/questions/3090302/how-do-i-get-the-object-if-it-exists-or-none-if-it-does-not-exist) members were attempted.
In the end an 'if' 'else' statement was inserted before the 'try' 'except' block in which the Order is created.
This retrieves the DiscountCode object from the database, if one exists, and if not, it sets the variable to 'None'. 
Now Orders, with or without discount codes, are successfully created within the Webhook Handler in the event of errors during the checkout process.

##### back to [top](#table-of-contents)
---

## Unresolved Issues

- Choosing the price options, 'Price High to Low' or 'Price Low to High' from the 
dropdown 'Sort by...' select on the 'Products' page does not take the 
discount price of a product into account.

- The pagination buttons rendered, especially on page one, do not make it obvious
to the viewer that the page range displayed does not reflect the total number of pages returned.

##### back to [top](#table-of-contents)
---
