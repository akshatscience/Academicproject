from datetime import datetime
from e_vote.forms import  CandidateRegistrationform, ElectionForm,Voters
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import user_passes_test
from datetime import datetime

# Create your views here.
global user_id
global election_id

def home(request):
    election=Election.objects.all()
    
    date=datetime.now()
    
    # for i in election:
    #     s=i.reg_start_date
    #     r=i.reg_end_date
    #     print(s,r)
    #     if s<=date and date<=r:
    #         print("true")

    return render(request,'home.html',{'election':election,'datetime':date})


# def admin_signup(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         email=request.POST.get('email')
#         signupform=User.objects.create_superuser(username,email,password)
        
#         signupform.save()
#         return redirect('admin_login')

#     return render(request,'admin_signup.html')



def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('election')


    return render(request,'admin_login.html')



#Create or Select Election
@user_passes_test(lambda u: u.is_superuser)
def election(request):
    
    electionform= ElectionForm()
    if request.method=='POST':
        name=request.POST.get('name')
        sdate=request.POST.get('sdate')
        edate=request.POST.get('edate')
        rsdate=request.POST.get('rsdate')
        redate=request.POST.get('redate')
        elect=Election(name=name,start_date=sdate,end_date=edate,reg_start_date=rsdate,reg_end_date=redate)
        elect.user=request.user
        elect.save()
        logout(request)
        return redirect('/')

    return render(request,'election.html',{'form':electionform})




#Voter data verification
def voter(request,pk):
    global user_id
    global election_id
    election_id=Election.objects.get(elction_id=pk)
    candidate_data=Candidate.objects.filter(election_id=pk)
    voter_auth=Voters()
    voters_id = Voter.objects.values_list('voter_id',flat=True)
    otp='1234'
    
    length=len(voters_id)
    low=0
    high=length-1
    if request.method=='POST':
        form=Voters(request.POST)
        if form.is_valid():
            user_id=form.cleaned_data['user_id']
            set_status = Voter.objects.get(voter_id=user_id)
            OTP=form.cleaned_data['OTP']
            user_id=int(user_id)
            if set_status.status==False:
               
                for _ in voters_id:
                    try:
                        mid =(low+high)//2
                        if voters_id[mid]==user_id and OTP==otp:
                            
                            return redirect('voting_page')

                        elif voters_id[mid]>user_id:
                        
                            high=mid-1

                        else:
                            low=mid+1  
                        
                    except:
                        return redirect('voter')
                

    return render(request,'voter.html',{'form':voter_auth,'candidate_data':candidate_data})


#winner 
def winner(request):
    max_vote=Candidate.objects.filter(election_id=election_id)
    
    vote={}
    max_v=[]
    for i in max_vote:
        max_v.append(i.vote_count)

    maximum_votes=max(max_v)
    for i in max_vote:
        vote[i.name,i.Candidate_photo]=i.vote_count
    for i,j in vote.items():
        if j==maximum_votes:
            winner=i
            break
    winner_name=winner[0]
    winner_photo=winner[1]
    return render(request,'winner.html',{'winner_name':winner_name,'winner_photo':winner_photo})
    

#Candidate_Data
def votes(request):
    
    candidate_data=Candidate.objects.filter(election_id=election_id)
    

    return render(request,'voting_page.html',{'candidates':candidate_data})




#Voting
def give_vote(request,pk):
    candidate_id=Candidate.objects.get(Candidate_id=pk)
    votes=Candidate.objects.get(Candidate_id=pk)
    voter_id=Voter.objects.get(voter_id=user_id)
    context={}
    if request.method=='POST':
        
        if request.POST.get('vote'):
            votes.vote_count+=1
            
            #print(votes.vote_count)
            votes.save()
            
            voter_id.status=True
            voter_id.save()
                
            return redirect('/') 


    return render(request,'vote_count.html',{'candidate':candidate_id})




#Candidate Data
def candidate(request):
    form=CandidateRegistrationform()
    #cand=Candidate.objects.all()
    
    if request.method=='POST':
        form=CandidateRegistrationform(request.POST,request.FILES)
        
        if form.is_valid():

            form.save()

            return redirect('/')

    return render(request,'candidate.html',{'form':form})

    

