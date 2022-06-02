from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('api/v1/products/', views.ProductListCreateAPIView.as_view(), name='products_view'),
    path('api/v1/products/<int:id>/', views.ProductDetailPutDeleteAPIView.as_view(), name='product_detail_view'),
    path('api/v1/add-comment/', views.CommentCreateAPIView.as_view(), name='add_comment_view'),
    path('api/v1/comment/<int:id>/', views.CommentPutDeleteAPIView.as_view(), name='edit_comment_view'),
    # path('api/v1/products/?user_related=/', views.UserProductsViewSet.as_view()),
    # path('api/v1/products/?ordering=/', views.UserProductsViewSet.as_view())


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)