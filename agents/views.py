from django.shortcuts import render
from .models import Agent, PollingStation
from django.db.models import Q

def agent_list(request):
    query = request.GET.get('search', '')
    
    # Initialize an empty dictionary to organize the agents
    organized_agents = {}

    # Fetch agents with related data
    agents = Agent.objects.all().select_related(
        'village', 
        'village__parish', 
        'village__parish__sub_county', 
        'village__parish__sub_county__county'
    )

    if query:
        agents = agents.filter(
            Q(agent_id__icontains=query) |
            Q(name__icontains=query) |
            Q(phone_number__icontains=query) |
            Q(village__name__icontains=query) |
            Q(village__parish__name__icontains=query) |
            Q(village__parish__sub_county__name__icontains=query) |
            Q(village__parish__sub_county__county__name__icontains=query)
        )

    # Organize agents by county, sub-county, and parish
    for agent in agents:
        county = agent.village.parish.sub_county.county.name
        subcounty = agent.village.parish.sub_county.name
        parish = agent.village.parish.name
        
        if county not in organized_agents:
            organized_agents[county] = {}
        if subcounty not in organized_agents[county]:
            organized_agents[county][subcounty] = {}
        if parish not in organized_agents[county][subcounty]:
            organized_agents[county][subcounty][parish] = []
        
        organized_agents[county][subcounty][parish].append(agent)

    context = {
        'organized_agents': organized_agents,
        'query': query
    }
    return render(request, 'agents/agent_list.html', context)
