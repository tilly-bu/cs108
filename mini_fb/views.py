from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from .models import Profile , StatusMessage
from .forms import CreateProfileForm, UpdateProfileForm , CreateStatusMessageForm
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.edit import CreateView , UpdateView , DeleteView


# Create your views here.

class ShowAllProfilesView(ListView):
    """list of all the profiles""" 
    model = Profile
    template_name = "mini_fb/show_all_profiles.html"
    context_object_name = "profiles" #list containing profiles from data base?

class ShowProfilePageView(DetailView): 
    '''Display a single profile'''
    model = Profile
    template_name = 'mini_fb/show_profile_page.html'
    context_object_name = 'Profile' 

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record to display for this page view
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary
        form = CreateStatusMessageForm() 
        context['create_status_form'] = form
        # return this context dictionary
        return context


class CreateProfileView (CreateView): 
    model = Profile
    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html'   


class UpdateProfileView (UpdateView): 
    "update an existing profile and store in database"

    model = Profile
    form_class = UpdateProfileForm
    template_name = 'mini_fb/update_profile_form.html'   


def post_status_message(request, pk):
    '''
    Process a form submission to post a new status message.
    '''

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':
        form = CreateStatusMessageForm(request.POST or None)

        if form.is_valid():

            # create the StatusMessage object with the data in the CreateStatusMessageForm
            status_message = form.save(commit=False) # don't commit to database yet
            # find the profile that matches the `pk` in the URL
            profile = Profile.objects.get(pk=pk)
            # attach FK profile to this status message
            status_message.profile = profile 
            status_message.save() # now commit to database

            image = form.save(commit=False) #create object without saving
            image.profile = profile 
            image.save() #store to database 

    # redirect the user to the show_profile_page view
    return redirect(reverse('show_profile_page', kwargs={'pk': pk}))


# def add_image(profile, pk): 
#     'custom view function to handle the submission of an image upload'

#     # find the profile for which we are submitting the status update ? 
#     profile = Profile.objects.get(pk=pk)


#     # read the request data into the CreateStatusMessage Form 
#     form = CreateStatusMessageForm(request.POST or None, request.FILES or None)
#     #Check if the form is valid and save the object to the database 

#     if form.is_valid(): 

#         image = form.save(commit=False) #create object without saving
#         image.profile = profile 
#         image.save() #store to database 

#     else: 
#         print("Error: Form is invalid!")

#     # redirect to a new URL , display profile page + status message
#     url = reverse('profile', kwargs={'pk':pk})
#     return redirect(url)


class DeleteStatusMessageView (DeleteView): 
    "Delete an existing profile and store in database"

    model = Profile

    template_name = 'mini_fb/delete_profile.html'

    def get_success_url(self): 
            'return URL to which we should be directed after delete' 
            pk = self.kwargs.get('pk')  
            pri





