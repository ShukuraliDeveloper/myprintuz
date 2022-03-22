from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('home2', views.home2View, name='home2'),
    path('account', views.accountView, name='account'),
    path('about-us', views.aboutView, name='aboutus'),
    path('checkout', views.checkoutView, name='checkout'),
    path('cart', views.cartView, name='cart'),
    path('compare', views.compareView, name='compare'),

    path('blog-classic', views.blog_classicView, name='blog-classic'),
    path('blog-grid', views.blog_gridView, name='blog-grid'),
    path('blog-left-sidebar', views.blog_left_sidebarView, name='blog-left-sidebar'),
    path('blog-list', views.blog_list, name='blog-list'),

    path('components', views.componentsView, name='components'),

    path('contact-us', views.contactusView, name='contact-us'),
    path('contact-us2', views.contactus2View, name='contact-us2'),

    path('faq', views.faqView,name='faq'),

    path('post', views.postView, name='post'),
    path('post-without-sidebar', views.post_without_sidebarView, name='post-without-sidebar'),

    path('product', views.productView, name='product'),
    path('product-alt', views.product_altView, name='product-alt'),

    path('shop-grid-3', views.shop_grid_3View, name='shop-grid-3'),
    path('shop-grid-4', views.shop_grid_4View, name='shop-grid-4'),
    path('shop-grid-5', views.shop_grid_5View, name='shop-grid-5'),
    path('shop-list', views.shop_listView, name='shop-list'),
    path('shop-right', views.shop_rightView ,name='shop-right'),

    path('track-order', views.track_orderView, name='track-order'),

    path('typograph', views.typographView, name='typograph'),
    path('wishlist', views.wishlistView, name='wishlist'),

]