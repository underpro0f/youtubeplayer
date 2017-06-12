from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Friend
from django.views.generic import TemplateView
from .forms import FriendForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your views here.
#@never_cache
#@login_required
class FriendView(TemplateView):
    template_name = "friendship.html"
    

    def get(self, request, *args, **kwargs):
        
        form = FriendForm()
        users = User.objects.exclude(id=request.user.id)
        #friend = get_object_or_404(Friend, current_user=request.user)
        query = request.GET.get("q")

        true_friends=[]
        

        if query:
            queryset_list = User.objects.filter(username=query)
        else:
            queryset_list = None

        #your followers
        drugs = Friend.who_added_user(request.user)
        friendlist = []
        #try to get or except None
        '''
        try:

            friend = Friend.objects.get(current_user=request.user)
            friends = friend.users.all()
            if friends:
                for fr in friends:
                    friendlist.append(fr)
                      
        except Friend.DoesNotExist:           
            friends = None
        '''
        friend, created = Friend.objects.get_or_create(current_user=request.user)
        friends = friend.users.all()
        '''
        for fr in friends:
            friendlist.append(fr)
        '''
        true_friends = []

        for friend in friends:
            friendlist.append(friend)
            
            for drug in drugs:
                 
                if drug.pk == friend.pk:
                    true_friends.append(drug)
                    drugs.remove(drug)
                    friendlist.remove(drug)
                


        context = {'form': form, 'users': users,
                   'friends': friends,
                   'drugs': drugs,
                   'object_list': queryset_list,
                   'true_friends': true_friends,
                   'friendlist': friendlist,
                   }
        return render(request,self.template_name, context)
    '''
    def post(self, request):
        form = FriendForm(request.POST)
        if form.is_valid():
            self.user = form.get_user()

            text = self.user

            return redirect('friend_index:friend_index')

        context = {'form': form, 'text': text}
        return render(request,self.template_name, context)
    '''
   
    
@never_cache
@login_required
def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
        return redirect('friend_index:friend_index')
    elif operation == 'remove':
        Friend.remove_friend(request.user, friend)
        return redirect('friend_index:friend_index')
    return redirect('friend_index:friend_index')

'''
@never_cache
@login_required
def search_friends(request):        
'''