import asyncio
from random import SystemRandom

def run(tasks, *, loop=None):
    """Run Asynchronous Tasks"""
    if loop is None:
        loop = asyncio.get_event_loop()
    # waiting for all tasks
    return loop.run_until_complete(asyncio.wait(tasks))

async def scanner(ip, port, loop=None):
    fut = asyncio.open_connection(ip, port, loop=loop)

    try:
        reader, writer = await asyncio.wait_for(fut, timeout=0.5) # This is where it is blocking?
        print("{}:{} Connected".format(ip, port))
    except asyncio.TimeoutError:
        pass
    # handle connection refused and bunch of others
    except Exception as exc:
        print('Error {}:{} {}'.format(ip, port, exc))

def scan(ips, ports, randomize=False):
    """Scan the ports"""
    loop = asyncio.get_event_loop()
    if randomize:
        rdev = SystemRandom()
        ips = rdev.shuffle(ips)
        ports = rdev.shuffle(ports)

    # let's pass list of task, not only one
    run([scanner(ip, port) for port in ports for ip in ips])


ips = [input("IP to scan: ")]
STEP = 256
for r in range(STEP+1, 65536, STEP):
    # print(r)
    ports = [str(r) for r in list(range(r-STEP, r))]
    scan(ips, ports)