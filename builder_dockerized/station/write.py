from tag_builder import filter_tags
import os
from in_place import InPlace
from zipfile import ZipFile

def create_python_directory():
    os.mkdir("python")

# create_python_directory()

def add_requirements(*requirements):
    with open("./python/requirements.txt", "w") as outbound:
        for requirement in requirements:
            outbound.write(f"{requirement}\n")

        
# add_requirements("numpy", "requests", "in_place")

# If upgrade is not being performed, the argument should just be 
# rm -rf /var/lib/apt/lists/*. Else, apt-get upgrade -y, followed by
# the aforementioned.

# if copy_requirements is not None, COPY requirements.txt /tmp
# if install_requirements is not None, pip install -r /tmp/requirements.txt && \\
# if upgrade is not None, apt-get upgrade -y && \\
# if upgrade_pip is not None, RUN pip install --upgrade pip && \\
# if remove_lists is not None, rm -rf /var/lib/apt/lists/*

def write_simple_root(
    tag, copy_requirements = None,
    upgrade_pip = None, install_requirements = None,
    update = None, upgrade = None, remove_lists = None
):
    with open("./python/Dockerfile", "w") as outbound:
        outbound.write(
f"""FROM python:{tag}
{copy_requirements}
{upgrade_pip}
{install_requirements}
{update}
{upgrade}
{remove_lists}
"""
        )
# write_simple_root(
#     "3.9.0a5-buster",
#     "COPY requirements.txt /tmp",
#     "RUN pip install --upgrade pip && \\",
#     "pip install -r /tmp/requirements.txt && \\",
#     "apt-get update && \\",
#     "apt-get upgrade -y && \\",
#     "rm -rf /var/lib/apt/lists/*"
# )


def write_sudo_with_pwd(
    tag, username, password, copy_requirements = None,
    install_requirements = None, upgrade = None
):
    with open("./python/Dockerfile", "w") as outbound:
        outbound.write(
f"""FROM python:{tag}
{copy_requirements}
RUN pip install --upgrade pip && \\
    {install_requirements}
    apt-get update && \\
    {upgrade}
    apt-get -y install sudo && \\
    rm -rf /var/lib/apt/lists/* && \\
    useradd --create-home {username} && \\
    echo "{username}:{password}" | chpasswd && \\
    echo "root:{password}" | chpasswd && \\
    sudo usermod -a -G sudo {username}
WORKDIR /home/{username}
USER {username}
"""
        )

# write_sudo_with_pwd(
#     "3.9.0a5-buster",
#     "dell", "password",
#     "COPY requirements.txt /tmp",
#     "pip install -r /tmp/requirements.txt && \\",
#     "apt-get upgrade -y && \\"
# )

def write_sudo_no_pwd(
    tag, username, copy_requirements = None,
    install_requirements = None, upgrade = None
):
    with open("./python/Dockerfile", "w") as outbound:
        outbound.write(
f"""FROM python:{tag}
{copy_requirements}
RUN pip install --upgrade pip && \\
    {install_requirements}
    apt-get update && \\
    {upgrade}
    apt-get -y install sudo && \\
    rm -rf /var/lib/apt/lists/*
ENV user {username}
RUN useradd -m -d /home/${{user}} ${{user}} && \\
    chown -R ${{user}} /home/${{user}} && \\
    adduser ${{user}} sudo && \\
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER ${{user}}
WORKDIR /home/${{user}}
"""
        )

# write_sudo_no_pwd(
#     "3.9.0a5-buster",
#     "user1",   
# )

def remove_none():
    with InPlace("./python/Dockerfile") as inbound:
        for line in inbound:
            line = line.replace("None", "")
            if line.strip():
                inbound.write(line)

# remove_none()

# Without upgrade
# This works
# write_sudo_no_pwd(
#     "3.9.0a5-buster",
#     "user1",
#     "COPY requirements.txt /tmp",
#     "pip install -r /tmp/requirements.txt && \\"
# )

# With upgrade
# This works
# write_sudo_no_pwd(
#     "3.9.0a5-buster",
#     "user1",
#     "COPY requirements.txt /tmp",
#     "pip install -r /tmp/requirements.txt && \\",
#     "apt-get upgrade -y && \\"
# )


def zip_dockerfile(directory):
    with ZipFile("py_docker.zip", "w") as outbound:
        for folder_name, subfolders, filenames in os.walk(directory):
            for filename in filenames:
                file_path = os.path.join(folder_name, filename)
                outbound.write(file_path)

# zip_dockerfile()
                





