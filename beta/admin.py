from django.conf import settings
from django.contrib import admin
from beta.models import BetaSignup

capture_first = getattr(settings, 'BETA_CAPTURE_FIRST', False)
capture_both  = getattr(settings, 'BETA_CAPTURE_BOTH', False)

class BetaSignupAdmin(admin.ModelAdmin):
    model = BetaSignup
    list_display = ['email']
    if capture_first or capture_both:
        list_display.append('first_name')
    if capture_both:
        list_display.append('last_name')
    list_display += ['contacted', 'registered']
    list_filter = ('contacted', 'registered')
    search_fields = ('email', '^first_name', '^last_name')

admin.site.register(BetaSignup, BetaSignupAdmin)

