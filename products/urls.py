from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('add-product/', views.ProductListCreateAPIView.as_view(), name='products_view'),
    path('product/<int:id>/', views.ProductDetailPutDeleteAPIView.as_view(), name='product_detail_view'),
    path('add-comment/', views.CommentCreateAPIView.as_view(), name='add_comment_view'),
    path('comment/<int:id>/', views.CommentPutDeleteAPIView.as_view(), name='edit_comment_view'),
    path('add-category/', views.CategoryCreateAPIView.as_view(), name='add_category_view'),
    path('category/<int:id>/', views.CategoryPutDeleteAPIView.as_view(), name='edit_category_view'),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)