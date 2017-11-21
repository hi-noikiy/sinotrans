from django.contrib import admin
from inspection.admin import my_admin_site


from .models import (
    PickingBill, 
    Waybill,
    )

class PickingBillInline(admin.TabularInline):
    model = PickingBill
    extra = 0
    max_num = 50

class PickingBillAdmin(admin.ModelAdmin):
    list_display = [
                "waybill",
                "number",
                # "product_id",
                # "product_name",
                # "dispatch_bill_number",
                "waybill_number",
                "product_total_number",
                "packing_total_number",
                "status",
                # "created",
                ]

    list_editable = [
                # "product_id",
                # "product_name",
                # "dispatch_bill_number",
                "waybill_number",
                "product_total_number",
                "packing_total_number",
                "status",
                ]

    search_fields = [
                "waybill",
                "number",
                # "product_id",
                # "product_name",
                # "dispatch_bill_number",
                "waybill_number",
                "product_total_number",
                "packing_total_number",
                "status",
                # "created",
                ]

    list_filter = [ "product_id","waybill_number","dispatch_bill_number"]

    view_on_site = False

    class Media:
        css = {
            "all": ("css/model_admin.css","css/picking.css")
        }
        js = ("js/jquery.min.js","js/model_admin.js",)

    class Meta:
        model = PickingBill

class WaybillAdmin(admin.ModelAdmin):
    list_display = [
                'number',
                "forwarder",
                "product_number",
                "packing_number",
    ]

    list_editable = [
                "forwarder",
                "product_number",
                "packing_number",
    ]

    search_fields = [
                'number',
                "forwarder",
                "product_number",
                "packing_number",
    ]


    list_filter = [ 
                "forwarder",
                "product_number",
                ]

    inlines = [
        PickingBillInline,
    ]

    view_on_site = False

    class Meta:
        model = Waybill        

    class Media:
        css = {
            "all": ("css/model_admin.css","css/picking.css")
        }
        js = ("js/jquery.min.js","js/model_admin.js",)

admin.site.register(PickingBill, PickingBillAdmin)
admin.site.register(Waybill, WaybillAdmin)

my_admin_site.register(PickingBill, PickingBillAdmin)
my_admin_site.register(Waybill, WaybillAdmin)